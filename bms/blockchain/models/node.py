import signal
from subprocess import Popen

import os
from django.conf import settings
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

    process_pid = models.IntegerField(
        default=0,
        verbose_name='pid процесса geth'
    )

    port = models.CharField(
        blank=True, null=True,
        default='',
        max_length=50,
        verbose_name='порт',
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

    def init(self):
        self.blockchain.init()

    def connect(self):
        # geth --networkid 5128794 --port 30259 --datadir ./chain-data --bootnodes enode://2fd46b0fce2cde2d0d2b77d6e5a0912e6caba6b461ce8089f34d1a5adbe83b10a3ff547cdf2363970d5c56788cc1c58c17234788adef127446a59e35f5c70371@5.23.52.206:30259
        process = Popen([settings.GETH,
                         '--networkid', self.blockchain.network_id,
                         '--port', self.port,
                         '--datadir', self.blockchain.data_dir(),
                         '--bootnodes', self.blockchain.enode])
        self.process_pid = process.pid
        self.save()
        return process

    def stop(self):
        if self.process_pid:
            os.kill(self.process_pid, signal.SIGTERM)
            self.process_pid = 0
            self.save()
