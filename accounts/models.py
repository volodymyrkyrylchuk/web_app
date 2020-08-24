from django.db import models


# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=124, unique=True, default=login)

    def __str__(self):
        return f'nickname - {self.nickname}, id - {self.id}, password - {self.password}'

class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    media = models.FileField(upload_to='static/uploads/')


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment_text = models.CharField(max_length=500)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)

