from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    payment_id = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    payment_time = models.TimeField()

    def __str__(self):
        # return f'{self.payment_id} - {self.user.last_name}'
        return f'{self.payment_id}'