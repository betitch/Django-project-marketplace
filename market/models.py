from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User     # Django のデフォルトの User クラスがある 

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="カテゴリ名",max_length=20)

    def __str__(self):
        return self.name                        # 管理サイトでの表示がわかりやすいようにする。


class Product(models.Model):
    # Category モデルの id （プライマリーキー？）を記録する
    # on_delete は紐付く Category が消された時の挙動 mocels.CASCADE カテゴリが消された時 Producut も消される。
    category = models.ForeignKey(Category,verbose_name="カテゴリ",on_delete=models.CASCADE)
    name = models.CharField(verbose_name="商品名", max_length=20)  # verbose_name は管理サイト表示用
    price = models.IntegerField(verbose_name='希望売却価格')

    # １対多でユーザーモデルと紐つける。 ユーザーはクラスを作らなくて良い。
    user = models.ForeignKey(User, verbose_name='出品者', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):            # これがあるから、index.html で product 変数を出力させると
        return self.name          # name が出力されるのか。     ← どうもそうらしい。      
          
class Cart(models.Model):
    product = models.ForeignKey(Product, verbose_name="商品", on_delete=models.CASCADE)  # 外部キー
    price = models.IntegerField(verbose_name='希望購入価格')

    # １対多でユーザーモデルと紐つける。
    user = models.ForeignKey(User, verbose_name='購入希望者', on_delete=models.CASCADE, null=True, blank=True)


class Message(models.Model):
    product = models.ForeignKey(Product, verbose_name="商品", on_delete=models.CASCADE)
    content = models.CharField(verbose_name="メッセージ", max_length=1000)

    dt = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    # １対多でユーザーモデルと紐つける。
    user = models.ForeignKey(User, verbose_name='投稿者', on_delete=models.SET_NULL, null=True, blank=True)
