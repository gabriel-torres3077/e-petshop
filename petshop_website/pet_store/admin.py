from django.contrib import admin
from .models import Category, Product, ProductImages, ProductReview


admin.site.register(Category)

class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]

    class Meta:
        model = Product

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductReview)
