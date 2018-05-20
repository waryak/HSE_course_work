from celery.result import AsyncResult
from django.db import models

from blockchain.models.blockchain import Blockchain
from bms.celery import app


class Contract(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='название'
    )

    source = models.TextField(
        verbose_name='исходный код'
    )

    blockchain = models.ForeignKey(
        Blockchain,
        on_delete=models.CASCADE,
        verbose_name='блокчейн'
    )

    class Meta:
        verbose_name = 'контракт'
        verbose_name_plural = 'контракты'

    def __str__(self):
        return self.title

    def deploy(self):
        pass

    def call_function(self, node, name, *args):
        # TODO
        self.blockchain.execute_code(node, 'CODE_TO_CALL_FUNCTION')

    def get_result(self, task_id):
        res = AsyncResult(task_id, app=app)
        if res.state == 'SUCCESS':
            return res.get()
        else:
            return None
