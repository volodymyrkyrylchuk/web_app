from django.urls import path
from accounts import views
from accounts.views import ProfileListView

app_name = 'publications'

urlpatterns = [

     path('show/<slug>', views.get_publication, name='get'),
     path('publication/<int:pk>/', views.get_publication, name='publication'),

]