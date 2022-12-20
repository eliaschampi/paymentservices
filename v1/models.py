from django.db import models
from django.utils.translation import gettext_lazy as _
from authentication.models import User


class Payment(models.Model):

    class Service(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    service = models.CharField(
        max_length=2,
        choices=Service.choices,
        default=Service.NETFLIX,
    )
    payment_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users')
    amount = models.FloatField(default=0.0)
