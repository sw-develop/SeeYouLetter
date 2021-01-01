import os

from django.db import models

from mysite import settings


class Product(models.Model):
    #편지지 이미지
    name = models.CharField(max_length=100) #한글 입력 글자 수 확인
    price = models.IntegerField()

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id'] #오름차순 정렬

class User(models.Model):
    #이메일 -> 형식 체크 가능
    senderEmail = models.EmailField(
        verbose_name='email',
        max_length=255,
    )

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id'] #오름차순 정렬

class Topic(models.Model):
    content = models.CharField(max_length=50)

class Letter(models.Model):
    #fk
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='letter_sender')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='letter_paper', null=True)
    topics = models.ManyToManyField(Topic, relaed_name='letter_topics', null=True)
    #받는 월 정하기
    MARCH = '3'
    JUNE = '6'
    DECEMBER = '12'
    DATE_OF_RECEIVE_LETTER = [
        (MARCH, 'March'),
        (JUNE, 'June'),
        (DECEMBER, 'December'),
    ]
    date = models.CharField(
        max_length=2,
        choices=DATE_OF_RECEIVE_LETTER,
        default=MARCH,
    )
    #font -> 여러 개 중 한 개 선택하는거로
    letter_content = models.TextField(blank=True) #편지 본문 작성 글자 수 확인
    page = models.IntegerField(default=0, null=True)
    photo_price = models.IntegerField(default=0, null=True)

    def price_of_letter(self):
        price = self.product.price + self.page*1000 + self.photo_price
        return price

    class Meta:
        db_table = 'letters'
        verbose_name = 'Letter'
        verbose_name_plural = 'Letters'
        ordering = ['id']  # 오름차순 정렬

