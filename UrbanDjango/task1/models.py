from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=7, decimal_places=2)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=8, decimal_places=3)  # MB
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers')

    def __str__(self):
        return f'{self.title} | {self.description}. Cost: {self.cost}'