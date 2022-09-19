from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Review, Comment
from .forms import CommentForm, UserReviewForm
from django.db.models import Q
from django.db.models import Count, Avg


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).order_by('-timestamp')
    template_name = 'index.html'
    paginate_by = 3


class ReviewListMostUpvotes(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).annotate(upvote_count=Count('upvotes')).order_by('-upvote_count')
    template_name = 'index.html'
    paginate_by = 3


class ReviewListOldest(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).order_by('timestamp')
    template_name = 'index.html'
    paginate_by = 3


class ReviewListAleType(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).filter(type='Ale').order_by('timestamp')
    template_name = 'index.html'
    paginate_by = 3


class ReviewListStoutType(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).filter(type='Stout').order_by('timestamp')
    template_name = 'index.html'
    paginate_by = 3


class ReviewListLagerType(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).filter(type='Lager').order_by('timestamp')
    template_name = 'index.html'
    paginate_by = 3


class ReviewListPaleColour(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).filter(colour='Pale').order_by('timestamp')
    template_name = 'index.html'
    paginate_by = 3


class ReviewListGoldenColour(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).filter(colour='Golden').order_by('timestamp')
    template_name = 'index.html'
    paginate_by = 3


class ReviewListAmberColour(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).filter(colour='Amber').order_by('timestamp')
    template_name = 'index.html'
    paginate_by = 3


class ReviewListDarkColour(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).filter(colour='Dark').order_by('timestamp')
    template_name = 'index.html'
    paginate_by = 3


class ReviewListBottled(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).filter(served_as=1).order_by('timestamp')
    template_name = 'index.html'
    paginate_by = 3


class ReviewListDraught(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).filter(served_as=2).order_by('timestamp')
    template_name = 'index.html'
    paginate_by = 3


class BeerReviewSingle(View):

    def get(self, request, pk, *args, **kwargs):
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

    queryset = None
    review = None
    primary_key = None

    def get(self, request, *args, **kwargs):
        
        queryset = Review.objects.filter(approved=True).order_by('?')
        RandomReview.queryset = queryset
        review = queryset.first()
        RandomReview.review = review
        primary_key = review.pk
        RandomReview.primary_key = primary_key
        # random_review = RandomReview.review
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

        review = get_object_or_404(RandomReview.queryset, pk=RandomReview.primary_key)
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

    


class SearchResultsView(generic.ListView):
    model = Review
    template_name = 'search_results.html'
    paginate_by = 4

    def querystring(self):
        querystring = self.request.GET.copy()
        querystring.pop(self.page_kwarg, None)
        encoded_querystring = querystring.urlencode()
        return encoded_querystring

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Review.objects.filter(
            Q(name__icontains=query)
            | Q(brewery__icontains=query)
            | Q(type__icontains=query)
            | Q(colour__icontains=query)
            | Q(hops__icontains=query)
            | Q(keywords__icontains=query)
            ).filter(approved=True)
        return object_list


class UserReviewsView(generic.ListView):
    model = Review
    template_name = 'user_reviews.html'

    def get(self, request, *args, **kwargs):
        """
        5 use cases:
        1 - user has written no reviews, hence len(user_queryset_all) == 0
        2 - user has written one review, and it is awaiting approval, hence len(user_queryset_all) == 1 and len(user_queryset_approved) == 0
        3 - user has written one or more reviews, but they all are awaiting approval, hence len(user_queryset_approved) == 0
        4 - user has written one or more reviews, but some are awaiting approval hence len(user_queryset_all) > len(user_queryset_approved)
        5 - user has written one or more reviews, and all are approved
        """
        user_queryset_all = Review.objects.filter(author=request.user)
        user_queryset_approved = Review.objects.filter(author=request.user).filter(approved=True)

        template_name = 'user_reviews.html'

        if len(user_queryset_all) == 0:
            context = {
                "object_list": user_queryset_all,
            }
            # Unlike below, no special context object key is needed
            # The template uses the empty tag of object_list
            return render(request, template_name, context)

        elif len(user_queryset_all) == 1 and len(user_queryset_approved) == 0:
            context = {
                "object_list": user_queryset_approved,
                "one_review_awaiting_approval": True,
                "all_reviews_awaiting_approval": False,
                "some_reviews_awaiting_approval": False,
                "no_reviews_awaiting_approval": False
            }
            return render(request, template_name, context)

        elif len(user_queryset_approved) == 0:
            context = {
                "object_list": user_queryset_approved,
                "all_reviews_awaiting_approval": True,
                "some_reviews_awaiting_approval": False,
                "no_reviews_awaiting_approval": False
            }
            return render(request, template_name, context)

        elif len(user_queryset_all) > len(user_queryset_approved):
            # user_queryset_all > 0 and user_queryset_approved > 0
            context = {
                "object_list": user_queryset_approved,
                "all_reviews_awaiting_approval": False,
                "some_reviews_awaiting_approval": True,
                "no_reviews_awaiting_approval": True
            }
            return render(request, template_name, context)

        elif len(user_queryset_all) == len(user_queryset_approved):
            context = {
                "object_list": user_queryset_approved,
                "all_reviews_awaiting_approval": False,
                "some_reviews_awaiting_approval": False,
                "no_reviews_awaiting_approval": True
            }
            return render(request, template_name, context)


class AddReviewView(generic.CreateView):

    model = Review
    form_class = UserReviewForm
    template_name = 'add_review.html'

    # def get(self, request, *args, **kwargs):
    #     return render(
    #         request,
    #         "user_review.html",
    #         {
    #             "user_review_form": UserReviewForm(),
    #             "reviewed": False
    #         }
    #     )

    # In previous versions, def get was used to display an empty user review form
    # in this build, form_class provides this, using the UserReviewForm in forms.py and the associated widgets and labels
    # def post is used to check the validity of the form, provide the user, 
    # handle cloudinary image uploading and the return render that sets reviewed to True so that the HTML changes to the success message

    def post(self, request, *args, **kwargs):

        user_review_form = UserReviewForm(request.POST, request.FILES)

        if user_review_form.is_valid():
            user_review_form.instance.author = request.user
            user_review = user_review_form.save(commit=False)
            user_review.save()
        else:
            user_review_form = UserReviewForm()

        context = {
            "user_review_form": UserReviewForm(),
            "reviewed": True
        }
        template_name = 'add_review.html'

        return render(request, template_name, context)


class UpdateReviewView(generic.UpdateView):

    model = Review
    template_name = 'update_review.html'
    form_class = UserReviewForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        user_update_form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=user_update_form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        user_update_form = self.get_form(form_class)

        if user_update_form.is_valid():
            user_update_form.instance.approved = False
            return self.form_valid(user_update_form, request)
        return self.form_invalid(user_update_form)

    def form_valid(self, user_update_form, request):
        self.object = user_update_form.save()

        return render(
            request,
            "update_review.html",
            {
                "update_review_form": UserReviewForm(),
                "updated": True
            }
        )


class DeleteReviewView(generic.DeleteView):
    model = Review
    template_name = 'delete_review.html'
    success_url = reverse_lazy('home')


class ReviewUpvote(View):

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)

        if review.upvotes.filter(id=request.user.id).exists():
            review.upvotes.remove(request.user)
            # if upvote exists, remove it

        else:
            review.upvotes.add(request.user)
            # if no upvote, add an upvote
            if review.downvotes.filter(id=request.user.id).exists():
                review.downvotes.remove(request.user)
                # if a downvote exists, remove it when adding a downvote

        return HttpResponseRedirect(reverse('review', args=[pk]))


class ReviewDownvote(View):

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)

        if review.downvotes.filter(id=request.user.id).exists():
            review.downvotes.remove(request.user)
            # if downvotes exists, remove it

        else:
            review.downvotes.add(request.user)
            # if no downvotes, add a downvote
            if review.upvotes.filter(id=request.user.id).exists():
                review.upvotes.remove(request.user)
                # if an upvote exists, remove it when adding a downvote

        return HttpResponseRedirect(reverse('review', args=[pk]))
