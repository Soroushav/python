from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Company(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    amount = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(1000)
        ])
    discount = models.PositiveSmallIntegerField(default=0,
                                                validators=[
                                                    MaxValueValidator(100)
                                                ])
    sold = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    JOB_CHOICES = (
        ('Custodian', 'Custodian'),
        ('Cashier', 'Cashier'),
        ('Manager', 'Manager'),
        ('Stock clerk', 'Stock clerk')
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(18)
        ])
    job = models.CharField(choices=JOB_CHOICES, max_length=20)

    def __str__(self) -> str:
        return self.first_name

class Customer(models.Model):
    LEVEL_CHOICES = (
        ('N', 'Normal'),
        ('G', 'Golden'),
    )

    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=11)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=1)

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='order')
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    time = models.DateTimeField()
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.product.name} by : {self.customer.name}'