from django.contrib import admin
from .models import Service, PaymentUser, ExpiredPayment

admin.site.register(Service)
admin.site.register(PaymentUser)
admin.site.register(ExpiredPayment)