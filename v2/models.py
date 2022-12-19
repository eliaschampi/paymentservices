from django.db import models
from v1.models import User

class Service(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    logo = models.CharField(max_length=100)

class PaymentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pay_users")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="ser_users")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_date = models.DateTimeField(null=False, blank=False)
    expiration_date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class ExpiredPayment(models.Model):
    payment_user = models.ForeignKey(PaymentUser, on_delete=models.CASCADE, related_name="expired_pay_users")
    penalti_fee_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
 
    