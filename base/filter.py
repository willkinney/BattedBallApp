import django_filters
from .models import battedBallData

class dataFilter(django_filters.FilterSet):

    class Meta:
        # get our data model
        model = battedBallData

        # ModelMultipleChoiceFilter allows us to use AND conditions while filtering
        # Example: Filtering on Judge, Aaron and HomeRun will return results where
        # Judge is the batter AND the play outcome was a homerun
        type = django_filters.ModelMultipleChoiceFilter( 
        queryset=battedBallData.objects.all())

        # Note here:
        # icontains - field has to contain the search
        # istartswith - field has to start with the search
        fields ={
            'BATTER_ID': ['icontains'],
            'BATTER': ['icontains'],
            'PITCHER_ID': ['icontains'],
            'PITCHER': ['icontains'],
            'GAME_DATE': ['icontains'],
            'LAUNCH_ANGLE': ['istartswith'],
            'EXIT_SPEED': ['istartswith'],
            'EXIT_DIRECTION': ['istartswith'],
            'HIT_DISTANCE': ['istartswith'],
            'HANG_TIME': ['istartswith'],
            'HIT_SPIN_RATE': ['istartswith'],
            'PLAY_OUTCOME': ['icontains'],
            'VIDEO_LINK': ['icontains'] 
            }
             
        sequence = ('BATTER_ID',
            'BATTER',
            'PITCHER_ID',
            'PITCHER',
            'GAME_DATE',
            'LAUNCH_ANGLE',
            'EXIT_SPEED',
            'EXIT_DIRECTION',
            'HIT_DISTANCE',
            'HANG_TIME',
            'HIT_SPIN_RATE',
            'PLAY_OUTCOME',
            'VIDEO_LINK')