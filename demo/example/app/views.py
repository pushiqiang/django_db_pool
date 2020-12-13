# -*- coding: utf-8 -*-
import uuid
import random
import time
import threading
from django.db import connection, transaction
from django.shortcuts import HttpResponse
from django.views import View

from app.models import User, Category


class TestView(View):
    def get(self, request, *args, **kwargs):
        """ORM和原生sql
        """
        User.objects.create(name=str(uuid.uuid4()), age=22)
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from app_user",)
            row = cursor.fetchone()

        return HttpResponse('good')


class TestTransactionView(View):
    def get(self, request, *args, **kwargs):
        """数据库事务
        """
        with transaction.atomic():
            User.objects.create(name=str(uuid.uuid4()), age=18)
            Category.objects.create(index=int(random.random() * 1000), name=str(uuid.uuid4()))

        return HttpResponse('transaction good')


class TestThreadingView(View):
    def get(self, request, *args, **kwargs):
        """多线程操作数据库
        """
        def operator_thread():
            User.objects.create(name=str(uuid.uuid4()), age=50)
            Category.objects.create(index=int(random.random() * 1000), name=str(uuid.uuid4()))
            time.sleep(5)

        threads = []
        for x in range(10):
            threads.append(threading.Thread(target=operator_thread))

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        return HttpResponse('transaction good')
