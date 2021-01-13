from django.shortcuts import render
from django.views import View
# Create your views here.
from beans_bill.utils.response_code import *

from .amazon_spider import *
from beans_bill.utils.response_code import *
from beans_bill.utils.comm_utils import *
from amazon_spiders.models import *
from django.core.paginator import Paginator


class AmazonSpiderView(View):
    """开启亚马逊爬虫"""

    def post(self, request):
        params = {'user_id': (1, str)}
        js, code = valid_body_js(request, params)
        if code != CODE_SUCCESS:
            logger.error("invalid param")
            return json_response(code)

        # 启动
        goods_info = thread_party_run('')

        return json_response(CODE_SUCCESS)


class AmazonSpiderListView(View):
    """亚马逊查询"""

    def post(self, request):
        params = {'time': (1, str), 'page_index': (1, int), 'page_size': (1, int)}
        js, code = valid_body_js(request, params)
        if code != CODE_SUCCESS:
            logger.error("invalid param")
            return json_response(code)

        # 启动
        goods_info = BestSeller.objects.filter(s_time__contains=js['time'])
        total = len(goods_info)
        paginator = Paginator(goods_info, js['page_size'])
        page_info = paginator.page(js['page_index'])

        goods_res = []
        for i in page_info:
            goods_res.append({
                'rank': i.rank,
                'name': i.name,
                'score': i.score,
                'price': i.price,
                'goods_url': i.goods_url,
                'img_url': i.img_url,
                'point': json_decode(i.point),
                'brand': i.brand,
                'questions': i.questions,
                's_time': i.s_time,
                'reviews': i.reviews,
                'goods_weight': i.goods_weight,
                'goods_size': i.goods_size,
            })

        rsp = {
            'goods_info': goods_res,
            'total': total
        }
        return json_response(CODE_SUCCESS, rsp)


class AmazonTestView(View):
    """开启亚马逊爬虫测试"""

    def post(self, request):
        params = {'user_id': (1, str)}
        js, code = valid_body_js(request, params)
        if code != CODE_SUCCESS:
            logger.error("invalid param")
            return json_response(code)

        # 启动
        logger.info("test:{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        return json_response(CODE_SUCCESS, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class AmazonBestTimeView(View):
    """亚马逊爬虫时间"""

    def post(self, request):
        params = {'time': (1, str)}
        js, code = valid_body_js(request, params)
        if code != CODE_SUCCESS:
            logger.error("invalid param")
            return json_response(code)

        time_list = BestSellerTime.objects.filter(spider_time__contains=js['time'])
        rsp = [i.spider_time for i in time_list]
        rsp = list(set(rsp))

        return json_response(CODE_SUCCESS, rsp)
