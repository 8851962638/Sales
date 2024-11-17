from django.contrib import admin
from .models import Product

# Register the Product model to make it accessible in the Django Admin interface
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'referral_fee', 'total_cost')  # Fields to display in list view
    search_fields = ('name',)  # Add search functionality based on product name

# Register the model with the admin site
admin.site.register(Product, ProductAdmin)
