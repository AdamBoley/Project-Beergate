from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('user_review/', views.AddReviewView.as_view(), name='user_review'),
    path('reviews/<int:pk>/', views.BeerReviewSingle.as_view(), name='review'),
    path('reviews/edit/<int:pk>/', views.UpdateReviewView.as_view(), name='update_review'),
    path('reviews/<int:pk>/remove', views.DeleteReviewView.as_view(), name='delete_review'),
    path('reviews/upvote/<int:pk>', views.ReviewUpvote.as_view(), name='review_upvote'),
    path('reviews/downvote/<int:pk>', views.ReviewDownvote.as_view(), name='review_downvote'),
]
