from django.db import models
from django.db.models import PROTECT

from users.models import CustomUser


class Advertisement(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to='advertisement/static/img/%Y/%m/%d')
    owner = models.ForeignKey(CustomUser, on_delete=PROTECT)

    def get_image_url(self):
        return self.image.url
