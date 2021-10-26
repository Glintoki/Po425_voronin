from django.contrib import admin
from .models import *

admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(ReceiptInvoice)
admin.site.register(Arrival)
admin.site.register(WarehouseWorker)
admin.site.register(Order)
admin.site.register(Consumption)
admin.site.register(ExpenditureInvoice)

