from django.contrib import admin
from .models import Profile, Publication, Comments


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'password', 'nickname')


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'profile_id', 'publication_date', 'author', 'image', 'file')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'publication', 'text')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Comments, CommentsAdmin)

