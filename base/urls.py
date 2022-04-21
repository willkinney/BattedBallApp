from http.client import HTTPResponse
from django.urls import path
from . import views
from base.views import home

urlpatterns = [
    # default URL
    path('', home.as_view(), name = "home"),
    # URL for data breakdown scatter plot page
    path(r'databreakdown/int:<_BATTER_ID>/dec:<_EXIT_SPEED>', views.databreakdown, name = "data breakdown"),
]
