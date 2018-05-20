from django.db import models
from django.utils.crypto import get_random_string

from blockchain.models.blockchain import Blockchain
from blockchain.tasks import run_command, execute_code


class Node(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='название')

    queue_name = models.CharField(
        max_length=100,
        verbose_name='название очереди'
    )

    blockchain = models.ForeignKey(
        Blockchain,
        on_delete=models.CASCADE,
        verbose_name='блокчейн'
    )

    class Meta:
        verbose_name = 'нода'
        verbose_name_plural = 'ноды'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = get_random_string(length=50)
        if not self.queue_name:
            self.queue_name = self.title
        super(Node, self).save(args, kwargs)

    def run_command(self, command):
        run_command.apply_async(
            (command,),
            queue=self.queue_name,
        )

    def execute_code(self, code):
        execute_code.apply_async(
            (code,),
            queue=self.queue_name,
        )
