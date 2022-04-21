from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from base.models import battedBallData
from .table import BallTable
from .filter import dataFilter

# home view contains the table of data and the search bars used for filtering
class home(SingleTableMixin, FilterView):
    model = battedBallData
    table_class = BallTable
    filterset_class = dataFilter
    template_name = 'home.html'

# data breakdown displays the plot of the dataset in a new page
def databreakdown(request, _BATTER_ID, _EXIT_SPEED):
    # Will populate these below to pass to HTML
    exit_velo = []
    launch_angle = []
    play_outcome = []

    # Order the data by exit speed for consistency
    info = battedBallData.objects.order_by('EXIT_SPEED')

    # Append to lists that will be passed databreakdown.html to use for scatter plot
    for row in info:
        exit_velo.append(row.EXIT_SPEED)
        launch_angle.append(row.LAUNCH_ANGLE)
        play_outcome.append(row.PLAY_OUTCOME)

    # Return the request to render the databreakdown page.
    # Also pass all of the needed data in the extra context dictionary.
    return render(request, 'databreakdown.html',
    {'BATTER_ID': _BATTER_ID,
    'EXIT_SPEED': _EXIT_SPEED,
    'exit_velo': exit_velo,
    'launch_angle': launch_angle,
    'play_outcome': play_outcome,
    })