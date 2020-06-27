from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Event(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.CharField(max_length=100)
    day = models.DateTimeField()
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str(self.user) + ": " + self.description

    def get_absolute_url(self):
        return reverse('home')

