from django.db import models
from letter.models import Letter
from pytz import timezone

class Customer(models.Model):
    letter = models.OneToOneField(Letter, on_delete=models.CASCADE, primary_key=True)
    senderName = models.CharField(max_length=100)
    senderPhone = models.CharField(max_length=14)
    senderFullAddress = models.CharField(max_length=100)
    senderDetailedAddress = models.CharField(max_length=100)
    senderZoneCode = models.IntegerField()
    receiverName = models.CharField(max_length=100)
    receiverPhone = models.CharField(max_length=14)
    receiverFullAddress = models.CharField(max_length=100)
    receiverDetailedAddress = models.CharField(max_length=100)
    receiverZoneCode = models.IntegerField()
    #우편방법
    MODE_OF_SEND_MAIL = [
        ('a', '일반우편'),
        ('b', '등기우편'),
    ]
    postMethod = models.CharField(
        max_length=5,
        choices=MODE_OF_SEND_MAIL,
        default='a',
    )

    #개인정보동의
    #환불정책동의

    def price_of_mail(self):
        price = 0
        if self.postMethod == 'b':
            price += 1000
        return price

    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class Order(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    letterName = models.CharField(max_length=100)
    letterPrice = models.IntegerField()
    page_price = models.IntegerField()
    photo_price = models.IntegerField(null=True, default=0)
    postMethod = models.CharField(max_length=20, default='a')
    postMethod_price = models.IntegerField()
    total_price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


