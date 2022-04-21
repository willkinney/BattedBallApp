from django.db import models
import django_filters
import django_tables2

# Create the model to hold the BattedBallData Excel file in SQLite
class battedBallData(models.Model):
    BATTER_ID = models.IntegerField()
    BATTER = models.TextField()
    PITCHER_ID = models.IntegerField()
    PITCHER = models.TextField()
    GAME_DATE = models.TextField()
    LAUNCH_ANGLE = models.FloatField()
    EXIT_SPEED = models.FloatField()
    EXIT_DIRECTION = models.FloatField()
    HIT_DISTANCE = models.FloatField()
    HANG_TIME = models.FloatField()
    HIT_SPIN_RATE = models.FloatField()
    PLAY_OUTCOME = models.TextField()
    #make the video_link the private key as the link will be unique for each AB
    VIDEO_LINK = models.URLField(primary_key = True)


