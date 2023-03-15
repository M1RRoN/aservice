from django.urls import path

from advertisement.views import AdvertisementView

urlpatterns = [
    path('', AdvertisementView.as_view(), name='advertisement'),
]
