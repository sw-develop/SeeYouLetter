from django.db import models
from letter.models import Letter

class Order(models.Model):
    letter = models.OneToOneField(Letter, on_delete=models.CASCADE, primary_key=True)
    sender = models.CharField(max_length=30)
    sender_phone_number = models.CharField(max_length=14)
    #이메일
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
        ('regular mail', '일반우편'),
        ('registered mail', '등기우편'),
    ]
    send_mail = models.CharField(
        max_length=20,
        choices=MODE_OF_SEND_MAIL,
        default='regular mail',
    )

    #개인정보동의
    #환불정책동의
    #최종가격



