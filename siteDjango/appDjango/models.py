from django.db import models
from django.utils import timezone



class Provider(models.Model):
    Provider_Surname = models.CharField(max_length=50)
    Provider_Name = models.CharField(max_length=50)
    Provider_Patronymic = models.CharField(max_length=50)
    Provide_Number = models.CharField(max_length=11)
    Provide_Address = models.CharField(max_length=100)



class ReceiptInvoice(models.Model):
    Receipt_Date = models.DateField(default=timezone)
    Receipt_Sum = models.IntegerField(default=0)
    Receipt_Price = models.IntegerField(default=0)
    Receipt_Id_Product = models.IntegerField(default=0)
    Receipt_Id_Provider = models.ForeignKey(Provider, on_delete=models.CASCADE)


class Arrival(models.Model):
    ID_Receipt_Invoice = models.ForeignKey(ReceiptInvoice, on_delete=models.CASCADE)
    ID_Worker = models.ForeignKey(ReceiptInvoice, on_delete=models.CASCADE)

class WarehouseWorker(models.Model):
    Worker_Surname = models.CharField(max_length=50)
    Worker_Name = models.CharField(max_length=50)
    Worker_Patronymic = models.CharField(max_length=50)
    Worker_Number = models.CharField(max_length=11)
    Worker_Address = models.CharField(max_length=100)
    Worker_Position = models.CharField(max_length=20)

class Product(models.Model):
    Product_Name = models.CharField(max_length=25)
    Product_Price = models.IntegerField(default=0)
    Product_Sum = models.IntegerField(default=0)
    Product_Expiration_Date = models.DateField(default=timezone)
    Product_Production_Date = models.CharField(default=timezone)


class Order(models.Model):
    Order_Sum = models.IntegerField(default=0)
    Order_Id_Product = models.IntegerField(default=0)
    Order_Name_Store = models.CharField(max_length=25)
    Order_Address = models.CharField(max_length=100)
    Order_Surname = models.CharField(max_length=50)
    Order_Name = models.CharField(max_length=50)
    Order_Patronymic = models.CharField(max_length=50)

class Consumption (models.Model):
    Consumption_Id_Worker = models.ForeignKey(Product, on_delete=models.CASCADE)
    Consumption_Id_Order = models.ForeignKey(Order, on_delete=models.CASCADE)

class ExpenditureInvoice (models.Model):
    Expend_Date = models.DateField(default=timezone)
    Expend_Price = models.IntegerField(default=0)
    Expend_Id_Consumption = models
    Expend_ID_Product = models.IntegerField(default=0)
    Expend_Sum = models.IntegerField(default=0)