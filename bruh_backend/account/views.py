# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView

from account.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
