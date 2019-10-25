from django.contrib.auth.models import User, Group
from rest_framework import serializers
from duckapp.duckapi.models import FeedingSession


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

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
