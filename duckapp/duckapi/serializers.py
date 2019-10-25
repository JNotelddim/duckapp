from rest_framework import serializers
from duckapp.duckapi.models import FeedingSession


class FeedingSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedingSession
        fields = [
            'feeding_time',
            'food',
            'food_type',
            'food_quantity',
            'location',
            'duck_count']
