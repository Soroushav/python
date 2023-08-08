from datetime import datetime
from django.utils import timezone
from .models import Employee, Product, Company, Order, Customer
from django.db.models import Q, F, Avg, Sum, Count

def young_employees(job: str):
    query = Employee.objects.filter(Q(age__lt=30) & Q(job=job))
    return query


def cheap_products():
    product = Product.objects.aggregate(average=Avg('price'))
    average = product['average']
    query = Product.objects.filter(price__lt=average).order_by('price')
    return query.values_list('name', flat=True)

def products_sold_by_companies():
    query = Company.objects.annotate(sum_of_sold=Sum('product__sold')).values_list('name', 'sum_of_sold')
    return query

def sum_of_income(start_date: str, end_date: str):
    date_format = "%Y-%m-%d"
    start_date = timezone.make_aware(datetime.strptime(start_date, date_format))
    end_date = timezone.make_aware(datetime.strptime(end_date, date_format))
    query = Order.objects.filter(time__range=[start_date, end_date]).aggregate(sum=Sum('price'))
    return query['sum']


def good_customers():

    query = Customer.objects.annotate(orders=Count('order')).filter(Q(level='G') & Q(order__gt=10))
    return query.values_list('name', 'phone')


def nonprofitable_companies():
    query = Company.objects.filter(product__sold__lt=100).annotate(count=Count('product')).filter(count__gte=4)
    return query.values_list('name', flat=True)
