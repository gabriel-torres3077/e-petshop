from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
"""
title = models.CharField(max_length=100)
    description = models.TextField()
    tags = TaggableManager()
    url = models.URLField(default='https://github.com/gabriel-torres3077?tab=repositories')
    image = models.ImageField(upload_to='portifolio/images', default='default.jpg')
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    """
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = 'Categorias'
        ordering = ('ordering', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % (self.slug)


# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='produtos', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    images = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=False)
    stock = models.IntegerField(default=1)

    class Meta:
        ordering = ('-created_at', )

    def save(self, *args, **kwargs):
        if not self.id:
            #create slug if object is new
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category, self.slug)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')


class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    user_review = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
