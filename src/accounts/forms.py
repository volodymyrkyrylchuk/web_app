from django.forms import ModelForm

from accounts.models import Profile

class ProfileBaseForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAddForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = '__all__'



class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = '__all__'
