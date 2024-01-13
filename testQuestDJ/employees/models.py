from django.db import models


class Positions(models.Model):
    name = models.CharField(max_length=254)
    weight = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Employees(models.Model):
    full_name = models.CharField(max_length=254)
    position = models.ForeignKey(Positions, on_delete=models.SET_NULL, null=True)
    acceptance_date = models.DateTimeField()
    email = models.EmailField(max_length=254)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.full_name