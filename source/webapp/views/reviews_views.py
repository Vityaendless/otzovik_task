from django.views.generic import CreateView, UpdateView, DeleteView, ListView, View
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib.auth.mixins import PermissionRequiredMixin

from ..models import Review, Product
from ..forms import ReviewForm
from ..helpers import Helper


class ReviewCreateView(CreateView):
    template_name = 'reviews/review_create.html'
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        return redirect('webapp:product_view', pk=product.pk)


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'reviews/review_update.html'
    model = Review
    form_class = ReviewForm
    permission_required = 'webapp.change_review'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def handle_no_permission(self):
        return redirect('webapp:403')

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review
    permission_required = 'webapp.delete_review'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def handle_no_permission(self):
        return redirect('webapp:403')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})


class NoModerateReviewsView(PermissionRequiredMixin, ListView):
    template_name = 'reviews/no_moderate_list.html'
    context_object_name = 'reviews'
    paginate_by = 10
    paginate_orphans = 1
    permission_required = 'webapp.see_no_moderate_reviews'

    def handle_no_permission(self):
        return redirect('webapp:403')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stars'] = Helper.stars
        return context

    def get_queryset(self):
        return Review.objects.filter(status=1).order_by('-created_at')

class ReviewAcceptView(View):
    permission_required = 'webapp.accept_review'

    def handle_no_permission(self):
        return redirect('webapp:403')

    def get(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs.get('pk'))
        review.status = 2
        review.save()
        return redirect('webapp:no_moderate_list')
