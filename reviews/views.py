from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.db.models import Count
from .models import Review
from .forms import CommentForm, UserReviewForm


class LandingPage(generic.ListView):
    """
    Base view to populate the landing page
    Defines the model, template name and pagination factor
    This view is not directly called, but serves as a base that -
    - is inherited by other views
    """
    model = Review
    template_name = 'index.html'
    paginate_by = 3


class ReviewList(LandingPage):
    """
    The default view to populate the landing page
    sorts reviews by timestamp in descending order
    Newest reviews appear first
    """
    queryset = Review.objects.filter(approved=True).order_by('-timestamp')


class ReviewListMostUpvotes(LandingPage):
    """
    A sorting view that populates the landing page
    sorts reviews by upvote count using annotate method
    """
    queryset = Review.objects.filter(approved=True).annotate(
        upvote_count=Count('upvotes')).order_by('-upvote_count')


class ReviewListOldest(LandingPage):
    """
    A sorting view that populates the landing page
    sorts reviews by timestamp in ascending order
    Oldest reviews appear first
    """
    queryset = Review.objects.filter(approved=True).order_by('timestamp')


class ReviewListAleType(LandingPage):
    """
    A filtering view that populates the landing page
    Filters out reviews that do not have a type of Ale
    """
    queryset = Review.objects.filter(approved=True).filter(
        type='Ale').order_by('timestamp')


class ReviewListStoutType(LandingPage):
    """
    A filtering view that populates the landing page
    Filters out reviews that do not have a type of Stout
    """
    queryset = Review.objects.filter(approved=True).filter(
        type='Stout').order_by('timestamp')


class ReviewListLagerType(LandingPage):
    """
    A filtering view that populates the landing page
    Filters out reviews that do not have a type of Lager
    """
    queryset = Review.objects.filter(approved=True).filter(
        type='Lager').order_by('timestamp')


class ReviewListPaleColour(LandingPage):
    """
    A filtering view that populates the landing page
    Filters out reviews that do not have a colour of Pale
    """
    queryset = Review.objects.filter(approved=True).filter(
        colour='Pale').order_by('timestamp')


class ReviewListGoldenColour(LandingPage):
    """
    A filtering view that populates the landing page
    Filters out reviews that do not have a colour of Golden
    """
    queryset = Review.objects.filter(approved=True).filter(
        colour='Golden').order_by('timestamp')


class ReviewListAmberColour(LandingPage):
    """
    A filtering view that populates the landing page
    Filters out reviews that do not have a colour of Amber
    """
    queryset = Review.objects.filter(approved=True).filter(
        colour='Amber').order_by('timestamp')


class ReviewListDarkColour(LandingPage):
    """
    A filtering view that populates the landing page
    Filters out reviews that do not have a colour of Dark
    """
    queryset = Review.objects.filter(approved=True).filter(
        colour='Dark').order_by('timestamp')


class ReviewListBottled(LandingPage):
    """
    A filtering view that populates the landing page
    Filters out reviews that were not served as bottled beers
    """
    queryset = Review.objects.filter(approved=True).filter(
        served_as=1).order_by('timestamp')


class ReviewListDraught(LandingPage):
    """
    A filtering view that populates the landing page
    Filters out reviews that were not served as draught beers
    """
    queryset = Review.objects.filter(approved=True).filter(
        served_as=2).order_by('timestamp')


class ReviewSingle(View):
    """
    The view used for rendering the review template
    Equivalent to a standard PostDetail-type view
    """

    def get(self, request, pk, *args, **kwargs):
        """
        Get method - retrieves the particular database record
        Requires a primary key to be supplied
        """
        queryset = Review.objects.filter(approved=True)
        review = get_object_or_404(queryset, pk=pk)
        comments = review.comments.filter(approved=True).order_by('timestamp')
        upvoted = False
        downvoted = False
        if review.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        if review.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        template_name = 'review.html'
        context = {
            "review": review,
            "comments": comments,
            "commented": False,
            "upvoted": upvoted,
            "downvoted": downvoted,
            "comment_form": CommentForm()
        }

        return render(request, template_name, context)

    def post(self, request, pk, *args, **kwargs):
        """
        Post method
        Functionally similar to Get method
        Handles comment submission
        """
        queryset = Review.objects.filter(approved=True)
        review = get_object_or_404(queryset, pk=pk)
        comments = review.comments.filter(approved=True).order_by('timestamp')
        upvoted = False
        downvoted = False
        if review.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        if review.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.save()
        else:
            comment_form = CommentForm()

        template_name = 'review.html'
        context = {
            "review": review,
            "comments": comments,
            "commented": True,
            "upvoted": upvoted,
            "downvoted": downvoted,
            "comment_form": CommentForm()
        }

        return render(request, template_name, context)


class RandomReview(View):
    """
    The view for rendering a random review
    Similar to BeerReviewSingle - has a get and a post method
    Prior to methods, declares 3 empty variables
    These allow the post method to render the same review -
    - when a comment is made
    """

    queryset = None
    review = None
    primary_key = None

    def get(self, request, *args, **kwargs):
        """
        Get method - retrieves a random review from the database
        Saves the queryset, review and review's primary key -
        - to class variables above
        """
        queryset = Review.objects.filter(approved=True).order_by('?')
        RandomReview.queryset = queryset
        review = queryset.first()
        RandomReview.review = review
        primary_key = review.pk
        RandomReview.primary_key = primary_key
        comments = review.comments.filter(approved=True).order_by('timestamp')
        upvoted = False
        downvoted = False
        if review.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        if review.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        template_name = 'review.html'
        context = {
            "review": review,
            "comments": comments,
            "commented": False,
            "upvoted": upvoted,
            "downvoted": downvoted,
            "comment_form": CommentForm(),
        }

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Post method - handles comment submission on the random review
        Takes in class variables as assigned by the Get method to render the -
        - same review when a comment is submitted
        """
        review = get_object_or_404(
            RandomReview.queryset, pk=RandomReview.primary_key)
        comments = review.comments.filter(approved=True).order_by('timestamp')
        upvoted = False
        downvoted = False
        if review.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        if review.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.save()
        else:
            comment_form = CommentForm()

        template_name = 'review.html'
        context = {
            "review": review,
            "comments": comments,
            "commented": True,
            "upvoted": upvoted,
            "downvoted": downvoted,
            "comment_form": CommentForm(),
        }

        return render(request, template_name, context)


class SearchResults(generic.ListView):
    """
    The view for rendering the search_results page
    Has three variables that set the model, template and pagination
    """
    model = Review
    template_name = 'search_results.html'
    paginate_by = 4

    def querystring(self):
        """
        querystring method
        Required for retaining the same queryset across multiple -
        - pagination pages
        """
        querystring = self.request.GET.copy()
        querystring.pop(self.page_kwarg, None)
        encoded_querystring = querystring.urlencode()
        return encoded_querystring

    def get_queryset(self):
        """
        get_queryset method
        Constructs a queryset using Q methods
        Returns an object_list for use within the template
        """
        query = self.request.GET.get('search')
        object_list = Review.objects.filter(
            Q(name__icontains=query) |
            Q(brewery__icontains=query) |
            Q(type__icontains=query) |
            Q(colour__icontains=query) |
            Q(hops__icontains=query) |
            Q(keywords__icontains=query)
            ).filter(approved=True)
        return object_list


class UserReviews(generic.ListView):
    """
    The view for rendering the user_reviews page
    """
    model = Review
    template_name = 'user_reviews.html'

    def get(self, request, *args, **kwargs):
        """
        Get method that constructs two querysets
        user_queryset_all retrieves all of a user's reviews, regardless -
        - of approval status
        user_queryset_approves retrieves only a user's approved reviews
        The method then considers 5 use cases:

        1 - user has written no reviews, -
        - hence len(user_queryset_all) == 0

        2 - user has written one review, and it is awaiting approval, hence -
        - len(user_queryset_all) == 1 and len(user_queryset_approved) == 0

        3 - user has written one or more reviews, but they all are -
        - awaiting approval, hence len(user_queryset_approved) == 0

        4 - user has written one or more reviews, but some are awaiting -
        - approval hence len(user_queryset_all) > len(user_queryset_approved)

        5 - user has written one or more reviews, and all are approved

        A context is constructed for each use case, -
        - and a return statment renders the page
        """
        user_queryset_all = Review.objects.filter(author=request.user)
        user_queryset_approved = Review.objects.filter(
            author=request.user).filter(approved=True)

        template_name = 'user_reviews.html'

        if len(user_queryset_all) == 0:
            context = {
                "object_list": user_queryset_all,
                "no_reviews_written": True
            }
            return render(request, template_name, context)

        elif len(user_queryset_all) == 1 and len(user_queryset_approved) == 0:
            context = {
                "object_list": user_queryset_approved,
                "one_review_awaiting_approval": True,
            }
            return render(request, template_name, context)

        elif len(user_queryset_approved) == 0:
            context = {
                "object_list": user_queryset_approved,
                "all_reviews_awaiting_approval": True,
            }
            return render(request, template_name, context)

        elif len(user_queryset_all) > len(user_queryset_approved):
            context = {
                "object_list": user_queryset_approved,
                "some_reviews_awaiting_approval": True,
            }
            return render(request, template_name, context)

        elif len(user_queryset_all) == len(user_queryset_approved):
            context = {
                "object_list": user_queryset_approved,
                "no_reviews_awaiting_approval": True
            }
            return render(request, template_name, context)


class AddReview(generic.CreateView):
    """
    The view for rendering the add_review page, where -
    - a user can add a review using the generated UserReviewForm
    Previous builds used a get method to construct the empty form
    The current build uses form_class to do this instead
    This has the advantage of including all associated widgets and labels
    """
    model = Review
    form_class = UserReviewForm
    template_name = 'add_review.html'

    def post(self, request, *args, **kwargs):
        """
        Post method that handles submission of the UserReviewForm
        If the form is valid, the add_review page is rendered again with -
        - the context, which is used to display a success message
        """
        template_name = 'add_review.html'

        user_review_form = UserReviewForm(request.POST, request.FILES)

        if user_review_form.is_valid():
            user_review_form.instance.name = (
                user_review_form.instance.name.title())
            user_review_form.instance.brewery = (
                user_review_form.instance.brewery.title())
            user_review_form.instance.type = (
                user_review_form.instance.type.capitalize())
            user_review_form.instance.colour = (
                user_review_form.instance.colour.capitalize())
            user_review_form.instance.keywords = (
                user_review_form.instance.keywords.lower())
            user_review_form.instance.author = request.user
            user_review = user_review_form.save(commit=False)
            user_review.save()

            context = {
                "user_review_form": UserReviewForm(),
                "reviewed": True
            }

            return render(request, template_name, context)

        else:
            user_review_form = UserReviewForm()

            context = {
                "user_review_form": UserReviewForm(),
                "reviewed": False,
                "failure": True
            }

            return render(request, template_name, context)


class UpdateReview(generic.UpdateView):
    """
    The view used for updating reviews on the front-end
    Use of the generic UpdateView pre-populates the form-
    -fields
    The 3 methods are necessary to automatically disapprove -
    - an updated review
    """

    model = Review
    template_name = 'update_review.html'
    form_class = UserReviewForm

    def get(self, request, *args, **kwargs):
        """
        Retrieves the review that is being updated
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        user_update_form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=user_update_form))

    def post(self, request, *args, **kwargs):
        """
        Handles submission of the updated review
        This is where the updated review is automatically disapproved
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        user_update_form = self.get_form(form_class)

        if user_update_form.is_valid():
            user_update_form.instance.name = (
                user_update_form.instance.name.title())
            user_update_form.instance.brewery = (
                user_update_form.instance.brewery.title())
            user_update_form.instance.type = (
                user_update_form.instance.type.capitalize())
            user_update_form.instance.colour = (
                user_update_form.instance.colour.capitalize())
            user_update_form.instance.keywords = (
                user_update_form.instance.keywords.lower())
            user_update_form.instance.approved = False
            return self.form_valid(user_update_form, request)
        else:
            return self.form_invalid(request)

    def form_valid(self, user_update_form, request):
        """
        Saves the updated review to the database
        Then renders the update_review page with a custom context
        The context is used to display a success message
        """
        self.object = user_update_form.save()
        template_name = self.template_name
        context = {
            "update_review_form": UserReviewForm(),
            "updated": True
        }

        return render(request, template_name, context)

    def form_invalid(self, request):
        """
        Handles invalid forms, such as when alcohol content is <0
        or when aroma, appearance, taste and aftertaste are <1 or >10
        """
        template_name = self.template_name
        context = {
            "update_review_form": UserReviewForm(),
            "updated": False,
            "failure": True
        }
        return render(request, template_name, context)


class DeleteReview(generic.DeleteView):
    """
    The view used for deleting a review on the front-end
    Does not use a get or post method
    The generic DeleteView handles all deletion functionality
    Upon success, redirects to the landing page
    """
    model = Review
    template_name = 'delete_review.html'
    success_url = reverse_lazy('home')


class ReviewUpvote(View):
    """
    The view used for upvoting a review
    Since upvoting takes place via a form -
    - all functionality is handled by the child post method
    """

    def post(self, request, pk):
        """
        Retrieves the review that is being upvoted
        If the review already has an upvote by the user, it is removed
        If no upvote is extant, an upvote is added
        And if there is an extant downvote by the user, it is removed -
        - when the upvote is added
        Upon completion, the user is redirected back to the review
        """
        review = get_object_or_404(Review, pk=pk)

        if review.upvotes.filter(id=request.user.id).exists():
            review.upvotes.remove(request.user)
            # if an upvote exists, remove it

        else:
            review.upvotes.add(request.user)
            # if there is no upvote, add an upvote
            if review.downvotes.filter(id=request.user.id).exists():
                review.downvotes.remove(request.user)
                # if a downvote exists, remove it when adding a downvote

        return HttpResponseRedirect(reverse('review', args=[pk]))


class ReviewDownvote(View):
    """
    The view used for downvoting a review
    Since downvoting takes place via a form -
    - all functionality is handled by the child post method
    """

    def post(self, request, pk):
        """
        Retrieves the review that is being downvoted
        If the review already has a downvote by the user, it is removed
        If no upvote is extant, a downvote is added
        And if there is an extant upvote by the user, it is removed -
        - when the downvote is added
        Upon completion, the user is redirected back to the review
        """
        review = get_object_or_404(Review, pk=pk)

        if review.downvotes.filter(id=request.user.id).exists():
            review.downvotes.remove(request.user)
            # if a downvote exists, remove it

        else:
            review.downvotes.add(request.user)
            # if there is no downvote, add a downvote
            if review.upvotes.filter(id=request.user.id).exists():
                review.upvotes.remove(request.user)
                # if an upvote exists, remove it when adding a downvote

        return HttpResponseRedirect(reverse('review', args=[pk]))


def http_404(request, exception):
    """
    Handles HTTP 404 Page Not Found errors
    """
    template_name = '404.html'
    return render(request, template_name)


def http_500(request):
    """
    Handles HTTP 500 Server Error errors
    """
    template_name = 'templates/500.html'
    return render(request, template_name)
