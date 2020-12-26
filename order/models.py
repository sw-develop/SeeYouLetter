from django.db import models
from letter.models import Letter

class Customer(models.Model):
    letter = models.OneToOneField(Letter, on_delete=models.CASCADE, primary_key=True)
    sender = models.CharField(max_length=30)
    #이메일 -> 형식 체크 가능
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
    )
    sender_addr = models.CharField(max_length=30) #우편번호랑 상세주소 다같이 저장되는건가?
    receiver = models.CharField(max_length=30)
    receiver_phone_number = models.CharField(max_length=14)
    receiver_addr = models.CharField(max_length=30)
    #우편방법
    MODE_OF_SEND_MAIL = [
        ('regular_mail', '일반우편'),
        ('registered_mail', '등기우편'),
    ]
    send_mail = models.CharField(
        max_length=20,
        choices=MODE_OF_SEND_MAIL,
        default='regular_mail',
    )

    #개인정보동의
    #환불정책동의

    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class Order(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    price = models.IntegerField()

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


