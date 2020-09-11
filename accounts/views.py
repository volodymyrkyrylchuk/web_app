from django.http.response import HttpResponseRedirect

from django.db.models import Q
from django.shortcuts import render

from accounts.forms import ProfileAddForm
from accounts.models import Profile, Publication
import os
from our_project.settings import BASE_DIR


# Create your views here.
def get_profiles_list(request):
    objects = Profile.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(Q(nickname__icontains=search) | Q(login__icontains=search))

    return render(
        request,
        'profiles.html',
        context={
            'result': objects,
            'search': search
        }
    )


def get_profile(request, id):
    profile = Profile.objects.get(id=id)
    return render(
        request,
        'profile.html',
        context={
            'profile': profile
        }
    )


def add_profile(request):
    if request.method == 'POST':
        form = ProfileAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profiles')

    elif request.method == 'GET':
        form = ProfileAddForm()

    return render(
        request,
        template_name='profile_add.html',
        context={
            'form': form
        }
    )

def get_publication(request, id):
    publication = Publication.objects.get(id=id)
    comments = publication.comments.all()
    return render(
        request,
        'publication.html',
        context={
            'date': publication.create_date,
            'file': os.path.join('../../', publication.media.url),
            'author': publication.author,
            'comments': comments
        }
    )