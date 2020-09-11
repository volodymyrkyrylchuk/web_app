from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from accounts.forms import ProfileAddForm
from accounts.models import Profile


class ProfilesListView(ListView):
    model = Profile
    template_name = 'profiles.html'
    context_object_name = 'result'

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(Q(nickname__icontains=search) | Q(login__icontains=search))
        return qs


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'
    pk_url_kwarg = 'item_id'


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profile_add.html'
    form_class = ProfileAddForm

    def get_success_url(self):
        return reverse('accounts:list')
