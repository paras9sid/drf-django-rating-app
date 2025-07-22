from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views


#View set
router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    # class based views paths 
    path('', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-detail'),

    #viewset
    path('',include(router.urls)),

    # url restructure for optimized search
    #to post review - differnet url
    path('<int:pk>/reviews/create/', views.ReviewCreate.as_view(), name='review-create'),

    # for get list,get one,put,delete
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    path('user-reviews/', views.UserReview.as_view(), name='user-review-detail'),
]
