# -*- coding: utf-8 -*-
# File              : async_task.py
# Author            : tjh
# Create Date       : 2020/08/05
# Last Modified Date: 2020/08/05
# Last Modified By  : tjh
# Reference         :
# Description       : 开启线程池
# ******************************************************
from concurrent.futures.thread import ThreadPoolExecutor


class AsyncTask(object):

    def __init__(self, nums=5):
        # 默认开启5个线程
        self.executor = ThreadPoolExecutor(nums)

    def submit_call_back(self, func, call_back, args):
        self.executor.submit(lambda p: func(*p), args).add_done_callback(call_back)

    def submit(self, func, args):
        self.executor.submit(lambda p: func(*p), args)

    def query_pool(self):
        # 参看线程池
        pass

    def shutdown_pool(self):
        # 关闭线程池
        pass