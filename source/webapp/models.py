from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


class IntegerRangeField(models.IntegerField):
    def __init__(self, min_value=None, max_value=None, **kwargs):
        self.validators = [MinValueValidator(min_value), MaxValueValidator(max_value)]
        super().__init__(**kwargs)


categories = [('1', 'Good'), ('2', 'Service')]
moderate_statuses = [('1', 'Moderate'), ('2', 'Approve'), ('3', 'Rejection')]


class AbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        abstract = True


class Product(AbstractModel):
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name="Title")
    category = models.CharField(max_length=30, null=False, blank=False, verbose_name='Category', choices=categories)
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Description")
    img = models.ImageField(upload_to='publications_images', null=True, blank=True, verbose_name='Avatar')
    avg_grade = models.FloatField(default=0, verbose_name='Avg grade')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.pk})



class Review(AbstractModel):
    product = models.ForeignKey(
        'webapp.Product', related_name='reviews', on_delete=models.CASCADE, verbose_name='Product'
    )
    author = models.ForeignKey(
        get_user_model(), default=1, related_name='reviews', on_delete=models.SET_DEFAULT, verbose_name='Author'
    )
    text = models.TextField(max_length=400, null=False, blank=False, verbose_name='Comment')
    grade = IntegerRangeField(min_value=1, max_value=5, null=False, blank=False, verbose_name='Grade')
    status = models.CharField(max_length=30, default=1, verbose_name='Status', choices=moderate_statuses)

    def __str__(self):
        return f'{self.pk} review'
