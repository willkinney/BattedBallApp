import django_tables2 as tables
from .models import battedBallData

class BallTable(tables.Table):

    # Add an additional column with the HTML from 'button.html'
    # The button HTML brings the user to the data breakdown page for
    # the selected at bat
    dataBreakdown = tables.TemplateColumn(template_name = 'button.html')

    class Meta:
        #get our data model
        model = battedBallData

        #html template for the table from django_tables2
        template_name = "django_tables2/bootstrap.html"

        #define the fields from the model
        fields = ('BATTER_ID',
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

        # Exclude batter id and pitcher id from displaying.
        # You can still filter on these fields, but they don't
        # need to be displayed.
        exclude = ('BATTER_ID',
        'PITCHER_ID'
        )
        
        # Define the order that the columns display in.
        # Shouldn't have to do this, but this fixes an issue where the order of columns
        # was changing when sorting.   
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