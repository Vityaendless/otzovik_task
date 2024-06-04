from django.urls import path
from django.views.generic import RedirectView

from .views import (IndexView, ProductCreateView, ProductView, ProductUpdateView, ProductDeleteView,
                    ReviewCreateView)


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update_view'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_view'),
    path('product/<int:pk>/review/add/', ReviewCreateView.as_view(), name='review_create'),
]
