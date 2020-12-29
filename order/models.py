from django.db import models
from letter.models import Letter

class Customer(models.Model):
    letter = models.OneToOneField(Letter, on_delete=models.CASCADE, primary_key=True)
    senderName = models.CharField(max_length=30)
    senderPhone = models.CharField(max_length=14)
    senderAddr = models.CharField(max_length=30)  # 우편번호랑 상세주소 다같이 저장되는건가?
    receiver = models.CharField(max_length=30)
    receiverPhone = models.CharField(max_length=14)
    receiverAddr = models.CharField(max_length=30)
    #우편방법
    MODE_OF_SEND_MAIL = [
        ('regular', '일반우편'),
        ('registered', '등기우편'),
    ]
    send_mail = models.CharField(
        max_length=20,
        choices=MODE_OF_SEND_MAIL,
        default='regular',
    )

    #개인정보동의
    #환불정책동의

    def price_of_mail(self):
        price = 0
        if self.send_mail == 'registered':
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
    letterPage_count = models.IntegerField()
    photo_price = models.IntegerField(null=True, default=0)
    send_mail = models.CharField(max_length=20, default='regular')
    total_price = models.IntegerField()

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


