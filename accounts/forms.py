from django.forms import ModelForm

from accounts.models import Profile


class ProfileAddForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
