from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views


#View set
router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    # class based views paths 
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-detail'),

    #filter watchlist
    path('list2/', views.WatchListGV.as_view(), name='watch-list'),

    # Stream Platform
    path('stream/', views.StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    #viewset
    path('',include(router.urls)),

    # url restructure for optimized search
    #to post review - differnet url
    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),

    # for get list,get one,put,delete
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    path('reviews/', views.UserReview.as_view(), name='user-review-detail'),
]
