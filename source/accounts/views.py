from django.shortcuts import redirect, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import MyUserCreationForm, UserChangeForm
from webapp.helpers import Helper


class RegisterView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.get_object().reviews.all()
        context['stars'] = Helper.stars
        return context


class UserEditView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('accounts:user_details', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UserPassesTestMixin, PasswordChangeView):
    template_name = 'user_password_change.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')

    def get_success_url(self):
        return reverse('accounts:user_details', kwargs={'pk': self.request.user.pk})
