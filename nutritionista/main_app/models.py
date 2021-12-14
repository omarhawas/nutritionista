from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


from django.contrib.auth.models import User
# Create your models here.
class Day(models.Model):
    date = models.DateField('date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse('detail', kwargs={'day_id': self.id})

