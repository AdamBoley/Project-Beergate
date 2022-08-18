from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('user_review/', views.UserReview.as_view(), name='user_review'),
    path('reviews/<int:pk>/', views.BeerReviewSingle.as_view(), name='review'),
    path('reviews/upvote/<int:pk>', views.ReviewUpvote.as_view(), name='review_upvote'),
    path('reviews/downvote/<int:pk>', views.ReviewDownvote.as_view(), name='review_downvote'),
]