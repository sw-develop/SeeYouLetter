from django.db import models

class Product(models.Model):
    #편지지 이미지
    name = models.CharField(max_length=100) #한글 입력 글자 수 확인
    price = models.IntegerField()

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id'] #오름차순 정렬

class Topic(models.Model):
    content = models.CharField(max_length = 100)

    class Meta:
        db_table = 'Topics'
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        ordering = ['id']  # 오름차순 정렬

class Letter(models.Model):
    #fk
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='letter_paper')
    #receiver -> me, others 둘 중 한 개 선택하는 거로도 가능? or 안해도?
    receiver = models.CharField(max_length=10)
    #font -> 여러 개 중 한 개 선택하는거로
    topic = models.ManyToManyField(Topic, blank=True)


    class Meta:
        db_table = 'letters'
        verbose_name = 'Letter'
        verbose_name_plural = 'Letters'
        ordering = ['id']  # 오름차순 정렬



class Content(models.Model):
    letter = models.OneToOneField(Letter, on_delete=models.CASCADE, primary_key=True)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    letter_content = models.CharField(max_length=100) #편지 본문 작성 글자 수 확인
    page = models.IntegerField()

    class Meta:
        db_table = 'Contents'
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

