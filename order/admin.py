from django.contrib import admin
from .models import Customer, Order

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'letter',
        'senderName',
        'senderPhone',
        'postMethod'
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'photo_price',
        'total_price',
        'created_date'
    )
