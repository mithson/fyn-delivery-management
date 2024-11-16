from django.db import models

# Create your models here
class Component(models.Model):
    name = models.CharField(max_length=100)
    repair_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"

class Issue(models.Model):
    REPAIR = 'REPAIR'
    REPLACE = 'REPLACE'
    CHOICES = [
        (REPAIR, 'Repair'),
        (REPLACE, 'Replace'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='issues')
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='issues')
    issue_type = models.CharField(max_length=10, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_cost(self):
        return self.component.repair_price if self.issue_type == self.REPAIR else self.component.purchase_price

class Transaction(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='transactions')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
