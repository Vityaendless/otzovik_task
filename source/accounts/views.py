from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, DetailView
from django.contrib.auth import get_user_model, login

from .forms import MyUserCreationForm
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
