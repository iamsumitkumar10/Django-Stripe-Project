from django.db import models
import uuid

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField() 

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    stripe_session_id = models.CharField(max_length=255, unique=True)
    amount = models.IntegerField()
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
