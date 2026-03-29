from django.db import models

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    spend = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Active')

    def __str__(self):
        return self.name