from django.db import models
from django.db.models import PROTECT

from users.models import CustomUser


class Application(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField()
    owner = models.ForeignKey(CustomUser, on_delete=PROTECT)

