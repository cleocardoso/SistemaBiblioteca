from django.conf.urls import url
from django.urls import path, include
from biblioteca.views import HomeView
app_name = 'biblioteca'

urlpatterns = [
   url(r'', HomeView.as_view())
]