from django.db import models

# Create your models here.
class CoinThrows(models.Model):
    throw_result = models.CharField(max_length=5)
    throw_date_time = models.DateTimeField(auto_now_add=True)
