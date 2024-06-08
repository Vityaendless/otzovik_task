from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegisterView, UserDetailView, UserEditView, UserPasswordChangeView


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_details'),
    path('user/<int:pk>/edit/', UserEditView.as_view(), name='edit_user'),
    path('user/<int:pk>/password_change/', UserPasswordChangeView.as_view(), name='user_password_change'),
]

#пагинация для отзывов
