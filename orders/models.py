from django.db import models
from django.contrib.auth.models import User
from catalogue.models import VinylRecord

from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # связь с пользователем!!! а не ко всему проекту, пофиксила где у каждого пользователя первый ордер это order #1, а не какой нибудь 5 и тд
    order_number = models.IntegerField()  # или можнл AutoField!
    product = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'order_number'], name='unique_order_for_user')
        ]

    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.filter(user=self.user).order_by('order_number').last()
            self.order_number = last_order.order_number + 1 if last_order else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    vinyl = models.ForeignKey(VinylRecord, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vinyl.title} (Order #{self.order.id})"
