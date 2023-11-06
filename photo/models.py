from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(
    verbose_name = 'カテゴリ',
    max_length = 20)
    
    def __str__(self):
        return self.title
    
class PhotoPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name = 'ユーザー',
        on_delete = models.CASCADE # カテゴリを消したときに記事も消す
    )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT # カテゴリを消したときに記事が存在してたら消させないようにする
    )
    title = models.CharField(
        verbose_name= 'タイトル',
        max_length=200
    )
    comment = models.TextField(
        verbose_name='コメント',
    )
    image1 = models.ImageField(
        verbose_name='イメージ',
        upload_to= 'photos'
    )
    image2 = models.ImageField(
    verbose_name='イメージ2',
    upload_to= 'photos',
    blank=True,
    null=True
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    def __str__(self):
        return self.title


