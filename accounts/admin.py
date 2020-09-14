from django.contrib import admin
from .models import Profile, Publication, Comment


admin.site.register(Profile)
admin.site.register(Publication)
admin.site.register(Comment)