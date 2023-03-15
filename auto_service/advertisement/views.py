from django.views.generic import ListView

from advertisement.models import Advertisement


class AdvertisementView(ListView):
    model = Advertisement
    template_name = 'advertisement/indextest.html'
