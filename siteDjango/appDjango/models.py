from django.db import models
from django.utils import timezone
class Provider(models.Model):
    Provider_Surname = models.CharField(max_length=50)
    Provider_Name = models.CharField(max_length=50)
    Provider_Patronymic = models.CharField(max_length=50)
    Provide_Number = models.CharField(max_length=11)
    Provide_Address = models.CharField(max_length=100)

class ReceiptInvoice(models.Model):
    ReceiptDate = models.DateField(default=timezone.now)
    ReceiptAmout = models.IntegerField(default=0)


