from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from accounts.forms import ProfileAddForm, ProfileEditForm
from accounts.models import Profile, Publication, Comments
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles.html'
    context_object_name = 'result'

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(Q(nickname__icontains=search) | Q(login__icontains=search))
        return qs

@method_decorator(login_required, name='dispatch')
class ProfileCreateView(CreateView, LoginRequiredMixin):
    model = Profile
    template_name = 'profile_add.html'
    form_class = ProfileAddForm

    def get_success_url(self):
        return reverse('accounts:list')


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'
    pk_url_kwarg = 'item_id'


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = '/'
    pk_url_kwarg = 'item_id'
    success_message = "Deleted successfully"




def get_publication(request, slug):
    publication = Publication.objects.get(id=slug)
    comments = Comments.objects.get(publication=publication)
    return render(request, 'publication.html', {'publication': publication,
                                                'comments': comments})


def edit_profile(request, slug):
    try:
        profile = Profile.objects.get(id=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Profile id-{slug} doesn`t exist')

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return  (f'/profiles/show/{slug}')
    elif request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    return render(request, template_name='profile_edit.html', context={'form': form})
