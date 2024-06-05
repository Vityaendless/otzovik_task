from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from ..models import Product
from ..forms import SimpleSearchForm, ProductForm
from ..helpers import Helper


class IndexView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'
    paginate_by = 10
    paginate_orphans = 1
    ordering = ('-created_at',)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(title__icontains=self.search_value) |
                Q(description__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    model = Product
    form_class = ProductForm


class ProductView(DetailView):
    model = Product
    template_name = 'products/product_details.html'

    def dispatch(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        reviews_count = product.reviews.count()
        if reviews_count >= 1:
            product.avg_grade = Helper.get_avg(product.reviews.all(), reviews_count)
            product.save()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        return context


class ProductUpdateView(UpdateView):
    template_name = 'products/product_update.html'
    model = Product
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    success_url = reverse_lazy('webapp:index')
