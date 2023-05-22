from django.db import models

# Create your models here.
class Houses(models.Model ):
    location=models.CharField(max_length=150)
    sqft=models.BigIntegerField()
    bathroom=models.IntegerField()
    bedroom=models.IntegerField()

    def __str__(self):
            return self.location