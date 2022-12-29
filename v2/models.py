from django.db import models
from authentication.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class Service(models.Model):

    class Service(models.TextChoices):
        YOUTUBE = 'YT', _('Youtube')
        SPOTIFY = 'SP', _('Spotify')
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    name = models.CharField(
        max_length=2,
        choices=Service.choices,
        default=Service.NETFLIX,
    )
    description = models.CharField(max_length=300)
    logo = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class PaymentUser(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pay_users")
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="ser_users")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_date = models.DateField(auto_now_add=True, null=False, blank=False)
    expiration_date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.service


class ExpiredPayment(models.Model):
    payment_user = models.ForeignKey(
        PaymentUser, on_delete=models.CASCADE, related_name="e_p_u")
    penalti_fee_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.payment_user

@receiver(post_save, sender=PaymentUser)
def create_expired_payment(sender, instance, created, **kwargs):
    if instance.payment_date > instance.expiration_date:
        ExpiredPayment.objects.create(
            payment_user_id=instance.id,
            penalti_fee_amount=100
        )

post_save.connect(create_expired_payment, sender=PaymentUser)
