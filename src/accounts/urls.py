from django.urls import path
from accounts import views
from accounts.views import ProfileListView, ProfileCreateView, ProfileDetailView, ProfileDeleteView


app_name = 'accounts'


urlpatterns = [
    path('', ProfileListView.as_view(), name='list'),
    path('add/', ProfileCreateView.as_view(), name='add'),
    path('show/<item_id>', ProfileDetailView.as_view(), name='show'),
    path('<item_id>/delete', ProfileDeleteView.as_view(), name='delete'),




    path('edit/<slug>', views.edit_profile, name='edit'),

]





