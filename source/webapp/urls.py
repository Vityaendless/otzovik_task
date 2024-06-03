from django.urls import path
from django.views.generic import RedirectView

from .views import IndexView, ProductCreateView, ProductView


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
]
