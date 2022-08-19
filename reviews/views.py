from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Review, Comment
from .forms import CommentForm, UserReviewForm


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=True).order_by('-timestamp')
    template_name = 'index.html'
    paginate_by = 4


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

        return render(
            request,
            "review.html",
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "upvoted": upvoted,
                "downvoted": downvoted,
                "comment_form": CommentForm()
            }
        )

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

        return render(
            request,
            "review.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "upvoted": upvoted,
                "downvoted": downvoted,
                "comment_form": CommentForm()
            }
        )


class AddReviewView(generic.CreateView):

    model = Review
    form_class = UserReviewForm
    template_name = 'user_review.html'

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

        return render(
            request,
            "user_review.html",
            {
                "user_review_form": UserReviewForm(),
                "reviewed": True
            }
        )


class UpdateReviewView(generic.UpdateView):

    model = Review
    template_name = 'update_review.html'
    form_class = UserReviewForm

    # def get(self, request, *args, **kwargs):
    #     return render(
    #         request,
    #         "update_review.html",
    #         {
    #             "update_review_form": UserReviewForm(),
    #             "updated": False
    #         }
    #     )

    # def post(self, request, *args, **kwargs):
    #     user_review_form = UserReviewForm(request.POST, request.FILES)

    #     if user_review_form.is_valid():
    #         user_review_form.instance.author = request.user
    #         user_review_form.instance.approved = False
    #         user_review = user_review_form.save(commit=False)
    #         user_review.save()
    #     else:
    #         user_review_form = UserReviewForm()

    #     return render(
    #         request,
    #         "update_review.html",
    #         {
    #             "update_review_form": UserReviewForm(),
    #             "updated": True
    #         }
    #     )

    # This post method appears to create a new duplicate record that is set to false, without setting the old record to false as well
    # see readme for further discussion of malicious users


class ReviewUpvote(View):

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)

        if review.upvotes.filter(id=request.user.id).exists():
            review.upvotes.remove(request.user)

        else:
            review.upvotes.add(request.user)

        return HttpResponseRedirect(reverse('review', args=[pk]))


class ReviewDownvote(View):

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)

        if review.downvotes.filter(id=request.user.id).exists():
            review.downvotes.remove(request.user)

        else:
            review.downvotes.add(request.user)

        return HttpResponseRedirect(reverse('review', args=[pk]))


