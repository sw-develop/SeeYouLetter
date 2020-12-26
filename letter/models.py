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


class Letter(models.Model):
    #fk
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='letter_paper')
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
    #receiver -> me, others 둘 중 한 개 선택하는 거로도 가능? or 안해도?
    receiver = models.CharField(max_length=10)
    #font -> 여러 개 중 한 개 선택하는거로


    class Meta:
        db_table = 'letters'
        verbose_name = 'Letter'
        verbose_name_plural = 'Letters'
        ordering = ['id']  # 오름차순 정렬



class Content(models.Model):
    letter = models.OneToOneField(Letter, on_delete=models.CASCADE, primary_key=True)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    letter_content = models.TextField() #편지 본문 작성 글자 수 확인
    page = models.IntegerField()

    class Meta:
        db_table = 'Contents'
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

