from django.db import models
from django.contrib.auth.models import User



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
    created = models.DateTimeField(auto_now_add=True)



class Publication(models.Model):
    publication_date = models.DateTimeField('Date of comment', auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/', null=False, blank=True)
    file = models.FileField(upload_to='static/files/', null=True, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.author, self.publication_date)


class Comments(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    text = models.TextField('Comment')

    def __str__(self):
        return self.text