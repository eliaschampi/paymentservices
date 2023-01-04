from rest_framework.throttling import UserRateThrottle


class CustomRateThrottle(UserRateThrottle):
    rate = "700/day"


class CustomPaymentRateThrottle(UserRateThrottle):
    rate = "300/day"
