from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'day_id': self.id})