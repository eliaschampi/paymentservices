from rest_framework.throttling import UserRateThrottle


class CustomRateThrottle(UserRateThrottle):
    rate = "70/day"


class CustomPaymentRateThrottle(UserRateThrottle):
    rate = "30/day"
