from django.db import models
from account.models import Voter

# Create your models here.

class Vote(models.Model):
    user = models.OneToOneField(Voter, on_delete=models.CASCADE)
    datetime_vote = models.DateTimeField(auto_now_add=True)
    bem_vote = models.CharField(null=True, blank=True, max_length=1)
    bpm_vote = models.CharField(null=True, blank=True, max_length=1)
    def __str__(self):
        return str(self.user)

class Vote2(models.Model):
    user = models.OneToOneField(Voter, on_delete=models.CASCADE)
    datetime_vote = models.DateTimeField(auto_now_add=True)
    bem_vote = models.CharField(max_length=1)
    def __str__(self):
        return str(self.user)
