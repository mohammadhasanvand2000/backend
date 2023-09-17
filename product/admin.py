from django.contrib import admin
from .models import Product, Categorythree,Categorytwo,KingCategory, Additional_field,Customer_comment,Bestselling,OrderItem,Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title',  'price', 'unit_of_measurement', 'Lowest_wholesale_amount', 'discribtion', 'introduction', 'Alloy', 'warranty', 'made_in', 'dimensions', 'in_dimensions', 'Weight', 'slug']
    list_filter = [ 'unit_of_measurement', 'made_in', 'warranty']
    search_fields = ['title', 'discribtion', 'introduction']

admin.site.register(Product, ProductAdmin)

admin.site.register(Additional_field)
admin.site.register(Customer_comment)
admin.site.register(Categorythree)
admin.site.register(Categorytwo)
admin.site.register(KingCategory)

admin.site.register(Bestselling)
admin.site.register(OrderItem)
admin.site.register(Order)
