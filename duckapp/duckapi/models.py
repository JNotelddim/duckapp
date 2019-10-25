from django.db import models


# Create your models here.
class FeedingSession(models.Model):
    # feeding time
    feeding_time = models.DateTimeField()

    # food
    food = models.CharField(max_length=100)
    # food_type
    food_type = models.CharField(max_length=100)
    # food quantity
    food_quantity = models.CharField(max_length=50)

    # location
    location = models.CharField(max_length=200)
    # number of ducks
    duck_count = models.IntegerField()
