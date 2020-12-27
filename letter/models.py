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
    sender = models.CharField(max_length=30)
    sender_phone_number = models.CharField(max_length=14)
    #이메일 -> 형식 체크 가능
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
    )
    sender_addr = models.CharField(max_length=30) #우편번호랑 상세주소 다같이 저장되는건가?

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
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    letter_content = models.TextField() #편지 본문 작성 글자 수 확인
    page = models.IntegerField()

    class Meta:
        db_table = 'letters'
        verbose_name = 'Letter'
        verbose_name_plural = 'Letters'
        ordering = ['id']  # 오름차순 정렬