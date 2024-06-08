from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegisterView


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    # path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    # path('<int:pk>/change/', UserChangeView.as_view(), name='user_change'),
    # path('<int:pk>/password_change/', UserPasswordChangeView.as_view(), name='user_password_change'),
]