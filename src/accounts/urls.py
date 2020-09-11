from django.urls import path
from accounts.views import ProfilesListView, ProfileCreateView, ProfileDetailView

app_name = 'accounts'

urlpatterns = [
    path('', ProfilesListView.as_view(), name='list'),
    path('add/', ProfileCreateView.as_view(), name='add'),
    path('show/<item_id>', ProfileDetailView.as_view(), name='show'),
]
