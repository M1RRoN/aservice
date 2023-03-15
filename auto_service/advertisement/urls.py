from django.conf.urls.static import static
from django.urls import path

from advertisement.views import AdvertisementView
from auto_service import settings

urlpatterns = [
    path('', AdvertisementView.as_view(), name='advertisement'),
]
urlpatterns += static(settings.STATIC_URL)