from django.db import models
from django.contrib.auth.models import User

class Financial_Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=100)
    income_level = models.TextField()
    credit_score = models.IntegerField()
    debt_ratio = models.FloatField(default=0.0)
    loan_amount = models.FloatField(default=0.0)
    loan_term = models.TextField()
    down_payment = models.FloatField(default=0.0)
    property_value = models.FloatField(default=0.0)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    message = models.TextField()

    class Meta:
        #Orders by recency of the notification
        ordering = ['-timestamp']

    def __str__(self):
        return self.message