from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views


urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # JWT
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
