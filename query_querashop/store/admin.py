from django.contrib import admin
from .models import Product, Order, Customer, Employee, Company

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'job']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'company', 'sold']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Company)

