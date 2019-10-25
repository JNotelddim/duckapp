from rest_framework import viewsets

from duckapp.duckapi.models import FeedingSession
from duckapp.duckapi.serializers import FeedingSessionSerializer


# Create your views here.
class FeedingSessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows feeding sessions to be viewed or edited
    """
    queryset = FeedingSession.objects.all()
    serializer_class = FeedingSessionSerializer
