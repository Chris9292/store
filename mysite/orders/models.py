from django.db import models
# Create your models here.

class Product(models.Model):

    code = models.CharField(max_length=10)
    factoryCode = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    dimensionMin = models.IntegerField(null=True)
    dimensionMax = models.IntegerField(null=True)
    color = models.CharField(max_length=10, null=True)
    direction = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=20, null=True)
    isStandard = models.BooleanField()
    group = models.IntegerField()

    def __str__(self) -> str:
        return f"Product code: {self.code}, description: {self.description}"