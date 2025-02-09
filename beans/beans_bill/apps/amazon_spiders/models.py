from django.db import models
from beans_bill.utils.models import BaseModel


# ["rank", "price", 'goods_url', 'name', 'brand', 'score', 'point', 'img_url', 'questions']
# Create your models here.
class BestSeller(BaseModel):
    """最佳售卖表"""
    seller_id = models.AutoField(verbose_name='ID', primary_key=True)
    rank = models.CharField(max_length=20, verbose_name='排名')
    price = models.CharField(max_length=100, verbose_name='价格')
    goods_url = models.CharField(max_length=300, verbose_name='访问页面url')
    brand = models.CharField(max_length=30, verbose_name='品牌或者店铺', default='')
    name = models.CharField(max_length=300, verbose_name='名称')
    score = models.CharField(max_length=30, verbose_name='分数')
    img_url = models.CharField(max_length=300, verbose_name='照片url')
    point = models.TextField(verbose_name='卖点')
    questions = models.CharField(max_length=10, verbose_name='访问数量')
    s_time = models.CharField(max_length=30, verbose_name='爬取日期')
    category = models.CharField(max_length=50, verbose_name='类目名', default='')
    reviews = models.CharField(max_length=100, verbose_name='评价数', default='')
    goods_weight = models.CharField(max_length=300, verbose_name='重量', default='')
    goods_size = models.CharField(max_length=100, verbose_name='尺寸', default='')
    goods_put_away = models.CharField(max_length=30, verbose_name='上架时间', default='')
    goods_asin = models.CharField(max_length=40, verbose_name='asin', default='')
    goods_model = models.CharField(max_length=40, verbose_name='型号', default='')
    goods_manufacturer = models.CharField(max_length=50, verbose_name='制造商', default='')
    goods_rank = models.CharField(max_length=500, verbose_name='亚马逊曾经排名', default='')

    class Meta:
        db_table = 'TAB_BEST_SELLER'
        verbose_name = '最佳售卖表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.seller_id, self.name)


class BestSellerTime(BaseModel):
    """最佳售卖表时间"""

    time_id = models.AutoField(verbose_name='ID', primary_key=True)
    spider_time = models.CharField(max_length=30, verbose_name='爬虫时间')

    class Meta:
        db_table = 'TAB_BEST_SELLER_TIME'
        verbose_name = '最佳售卖表时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.time_id, self.spider_time)
