from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from duckapp.duckapi.models import FeedingSession
from duckapp.duckapi.serializers \
    import UserSerializer, GroupSerializer, FeedingSessionSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class FeedingSessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows feeding sessions to be viewed or edited
    """
    queryset = FeedingSession.objects.all()
    serializer_class = FeedingSessionSerializer
