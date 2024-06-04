from django.views.generic import CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect, reverse

from ..models import Review, Product
from ..forms import ReviewForm


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


class ReviewUpdateView(UpdateView):
    template_name = 'reviews/review_update.html'
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})
