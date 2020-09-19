from django.contrib import admin


from .models import Profile, Publication, Comments, Following


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['bio', 'birth_date']


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['publication_date', 'author']


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['author', 'text']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Comments)
admin.site.register(Following)