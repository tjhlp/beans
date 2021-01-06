# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-12-30 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestSeller',
            fields=[
                ('Crt_Time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('Upd_Time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('seller_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=20, verbose_name='排名')),
                ('price', models.CharField(max_length=20, verbose_name='价格')),
                ('goods_url', models.CharField(max_length=100, verbose_name='访问页面url')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('score', models.CharField(max_length=30, verbose_name='分数')),
                ('img_url', models.CharField(max_length=100, verbose_name='照片url')),
                ('point', models.TextField(verbose_name='卖点')),
                ('questions', models.CharField(max_length=10, verbose_name='访问数量')),
                ('s_time', models.CharField(max_length=10, verbose_name='爬取日期')),
            ],
            options={
                'verbose_name': '最佳售卖表',
                'verbose_name_plural': '最佳售卖表',
                'db_table': 'TAB_BEST_SELLER',
            },
        ),
    ]
