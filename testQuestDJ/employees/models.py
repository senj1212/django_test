from django.db import models


class Positions(models.Model):
    name = models.CharField(max_length=254)
    weight = models.PositiveSmallIntegerField()


class Employees(models.Model):
    full_name = models.CharField(max_length=254)
    position = models.ForeignKey(Positions, on_delete=models.SET_NULL, null=True)
    acceptance_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
    manager = models.PositiveIntegerField()