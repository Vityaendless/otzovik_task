from django.urls import path

from .views import (IndexView, ProductCreateView, ProductView, ProductUpdateView, ProductDeleteView,
                    ReviewCreateView, ReviewUpdateView, ReviewDeleteView, permission_denied,
                    NoModerateReviewsView, ReviewAcceptView)


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update_view'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_view'),
    path('product/<int:pk>/review/add/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('review/no_moderate/', NoModerateReviewsView.as_view(), name='no_moderate_list'),
    path('review/<int:pk>/accept/', ReviewAcceptView.as_view(), name='accept_review'),
    path('403/', permission_denied, name='403'),
]
