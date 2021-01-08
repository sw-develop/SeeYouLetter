import os

from django.db import models

class Product(models.Model):
    #편지지 이미지
    name = models.CharField(max_length=100) #한글 입력 글자 수 확인
    price = models.IntegerField()

    def __str__(self):
        return 'name : {}'.format(self.name)

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

    def __str__(self):
        return 'email : {}'.format(self.senderEmail)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id'] #오름차순 정렬

class Topic(models.Model):
    content = models.CharField(max_length=50)

    class Meta:
        db_table = 'topics'
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        ordering = ['id'] #오름차순 정렬

class Letter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='letter_sender', null=True)
    paper = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='letter_paper', null=True)
    SelectedQuestions = models.ManyToManyField(Topic, related_name='letter_topics', blank=True)
    month = models.CharField(max_length=20, null=True)
    font = models.CharField(max_length=20, null=True)
    letterContent = models.TextField(blank=True) #편지 본문 작성 글자 수 확인
    page = models.IntegerField(default=0, null=True)
    photo_price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return 'user : {} letter : {}'.format(self.user, self.id)

    def price_of_page(self):
        price = (self.page-2)*1000
        return price

    def price_of_letter(self):
        price = self.paper.price + self.price_of_page() + self.photo_price
        return price

    class Meta:
        db_table = 'letters'
        verbose_name = 'Letter'
        verbose_name_plural = 'Letters'
        ordering = ['id']  # 오름차순 정렬
        get_latest_by = 'pk'

