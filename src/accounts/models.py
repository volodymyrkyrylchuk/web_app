from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'nickname - {self.nickname}, id - {self.id}, password - {self.password}'


class Following(models.Model):
    profile_id = models.ForeignKey(Profile, related_name="following", on_delete=models.CASCADE)
    following_profile_id = models.ForeignKey(Profile, related_name="followers", on_delete=models.CASCADE)

    # You can even add info about when user started following
    created = models.DateTimeField(auto_now_add=True)





