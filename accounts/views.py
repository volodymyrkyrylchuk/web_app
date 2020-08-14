from django.db.models import Q
from django.shortcuts import render
from accounts.models import Profile


# Create your views here.
def get_profiles_list(request):
    objects = Profile.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(Q(nickname__icontains=search) | Q(login__icontains=search))

    iterator = (f'{obj.nickname} - {obj.login}' for obj in objects)
    result = '<br>'.join(iterator)
    return render(request, 'profiles.html', context={'result': result})
