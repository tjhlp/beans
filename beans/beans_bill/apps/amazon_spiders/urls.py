from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^amazon/spider/$', views.AmazonSpiderView.as_view()),
    url(r'^amazon/best_seller_list/$', views.AmazonSpiderListView.as_view()),
    url(r'^amazon/test/$', views.AmazonTestView.as_view()),
    url(r'^amazon/best_time/list/$', views.AmazonBestTimeView.as_view()),

]
