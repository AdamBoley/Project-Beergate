from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('most_upvotes/', views.ReviewListMostUpvotes.as_view(), name='most_upvotes'),
    path('oldest/', views.ReviewListOldest.as_view(), name='oldest'),
    path('ales/', views.ReviewListAleType.as_view(), name='ales'),
    path('stouts/', views.ReviewListStoutType.as_view(), name='stouts'),
    path('lagers/', views.ReviewListLagerType.as_view(), name='lagers'),
    path('pale_beers/', views.ReviewListPaleColour.as_view(), name='pale'),
    path('golden_beers/', views.ReviewListGoldenColour.as_view(), name='golden'),
    path('amber_beers/', views.ReviewListAmberColour.as_view(), name='amber'),
    path('dark_beers/', views.ReviewListDarkColour.as_view(), name='dark'),
    path('bottled_beers/', views.ReviewListBottled.as_view(), name='bottled'),
    path('draught_beers/', views.ReviewListDraught.as_view(), name='draught'),
    path('add_review/', views.AddReviewView.as_view(), name='add_review'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('user_reviews/', views.UserReviewsView.as_view(), name='user_reviews'),
    path('reviews/<int:pk>/', views.BeerReviewSingle.as_view(), name='review'),
    path('reviews/edit/<int:pk>/', views.UpdateReviewView.as_view(), name='update_review'),
    path('reviews/<int:pk>/remove', views.DeleteReviewView.as_view(), name='delete_review'),
    path('reviews/upvote/<int:pk>', views.ReviewUpvote.as_view(), name='review_upvote'),
    path('reviews/downvote/<int:pk>', views.ReviewDownvote.as_view(), name='review_downvote'),
]
