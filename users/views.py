from rest_framework.generics import ListAPIView
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileListView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
