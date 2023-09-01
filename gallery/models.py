from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField(default=timezone.datetime.now())
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return f"{self.author}"
