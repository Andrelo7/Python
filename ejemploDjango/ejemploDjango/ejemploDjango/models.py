from django.db import models

product_status = [
    (1, 'NS200')
    (2, 'DUKE200')
    (3, 'XR250')
]

class Product (models.Model):
    title = models.CharField(max_length=50)
    status = models.IntegerField(
        null=False, blank=False,
        choices= product_status
    )
    def __str__(self):
        return self.title