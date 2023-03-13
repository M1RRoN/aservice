from django.contrib.auth.models import AbstractUser, models


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_joined = models.DateTimeField()




