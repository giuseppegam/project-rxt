from django.urls import path

from waze.views import TrafficAlertView, TrafficJamView

urlpatterns = [
    path('traffic-alerts/', TrafficAlertView.as_view(), name='traffic-alerts'),
    path('traffic-jams/', TrafficJamView.as_view(), name='traffic-jams'),
]
