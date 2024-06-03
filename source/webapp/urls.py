from django.urls import path
from django.views.generic import RedirectView

from .views import IndexView


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
