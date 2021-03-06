from django.db import models
from letter.models import Letter
from pytz import timezone

class Customer(models.Model):
    letter = models.OneToOneField(Letter, on_delete=models.CASCADE, primary_key=True)
    senderName = models.CharField(max_length=100, null=True)
    senderPhone = models.CharField(max_length=20, null=True)
    senderFullAddress = models.CharField(max_length=200, null=True)
    senderDetailedAddress = models.CharField(max_length=200, null=True)
    senderZoneCode = models.IntegerField(null=True)
    receiverName = models.CharField(max_length=100, null=True)
    receiverPhone = models.CharField(max_length=20, null=True)
    receiverFullAddress = models.CharField(max_length=200, null=True)
    receiverDetailedAddress = models.CharField(max_length=200, null=True)
    receiverZoneCode = models.IntegerField(null=True)
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

    def __str__(self):
        return '{}'.format(self.letter)

    def price_of_mail(self):
        price = 1500
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

    def __str__(self):
        return '{}'.format(self.customer)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


