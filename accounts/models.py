from django.db import models


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=124, unique=True, default=login)

    def __str__(self):
        return f'nickname - {self.nickname}, id - {self.id}, password - {self.password}'


class Publication(models.Model):
    id = models.AutoField(primary_key = True)
    publication_date = models.DateTimeField('published', auto_now=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    media = models.ImageField(upload_to='media/', null=False, blank=True)

    def __str__(self):
        return f'published by {self.author} on {self.publication_date}'


class Comment(models.Model):
    id = models.AutoField(primary_key = True)
    comment_text = models.CharField(max_length=250, default=None)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, related_name='comments', on_delete=models.CASCADE)

def __str__(self):
        return f'commented by {self.author}'
