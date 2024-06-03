from django.urls import path
from django.views.generic import RedirectView

from .views import IndexView, ProductCreateView


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
]
