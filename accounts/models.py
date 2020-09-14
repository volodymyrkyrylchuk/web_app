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
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    media = models.FileField(upload_to='static/uploads/')

    def __str__(self):
        return f'author - {self.author}, date - {self.create_date}'


class Comment(models.Model):
    id = models.AutoField(primary_key = True)
    comment_text = models.TextField(max_length=500, default=None)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, related_name='comments', on_delete=models.CASCADE)

