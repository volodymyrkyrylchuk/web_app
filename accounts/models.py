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
    publication_date = models.DateTimeField('Date of comment', auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=False, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.author, self.publication_date)


class Comments(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)



