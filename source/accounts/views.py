from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, login

from .forms import MyUserCreationForm


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
