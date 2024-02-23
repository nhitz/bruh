from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import api
from .views import CustomTokenObtainPairView

urlpatterns = [
    path("me/", api.me, name="me"),
    path("signup/", api.signup, name="signup"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("friends/<uuid:pk>/", api.friends, name="friends"),
    path(
        "friends/<uuid:pk>/request/",
        api.send_friendship_request,
        name="send_friendship_request",
    ),
    path("friends/<uuid:pk>/<str:status>/", api.handle_request, name="handle_request"),
]
