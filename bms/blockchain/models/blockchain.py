import signal
from subprocess import Popen, PIPE, call

import os
from django.conf import settings
from django.db import models


class Blockchain(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='название'
    )

    genesis_block = models.TextField(
        blank=True, null=True,
        default='',
        verbose_name='Genesis block',
    )

    network_id = models.CharField(
        blank=True, null=True,
        default='',
        max_length=50,
        verbose_name='network id',
    )

    port = models.CharField(
        blank=True, null=True,
        default='',
        max_length=50,
        verbose_name='порт',
    )

    enode = models.CharField(
        blank=True, null=True,
        default='',
        max_length=200,
        verbose_name='enode',
    )

    process_pid = models.IntegerField(
        blank=True, null=True,
        verbose_name='pid процесса geth'
    )

    class Meta:
        verbose_name = 'блокчейн'
        verbose_name_plural = 'блокчейны'

    def __str__(self):
        return self.title

    def roll_back(self):
        for node in self.node_set.all():
            # TODO
            node.run_command('ROLLBACK_COMMAND')

    def run_nodes(self):
        for node in self.node_set.all():
            # TODO
            node.run_command('RUN_COMMAND')

    def data_dir(self):
        return f'./data/{self.title}_data/'

    def init(self):
        # geth init GenesisBlock.json --datadir ./chain-data/
        call(['mkdir', self.data_dir()])
        genesis_block_file = self.data_dir() + 'genesis_block.json'
        f = open(genesis_block_file, 'w+')
        f.write(self.genesis_block)
        f.close()
        call([settings.GETH,
              'init',
              genesis_block_file,
              '--datadir', self.data_dir()])

    def start(self):
        # geth --networkid 5128794 --port 30259 --datadir my_chain_data/
        # stop by process.terminate()
        process = Popen([settings.GETH,
                         '--networkid', self.network_id,
                         '--port', self.port,
                         '--datadir', self.data_dir()])
        self.process_pid = int(process.pid)
        self.save()
        return process

    def stop(self):
        if self.process_pid:
            os.kill(self.process_pid, signal.SIGTERM)
            self.process_pid = 0
            self.save()

    def get_enode(self):
        # geth attach data/my_chain_data/geth.ipc --exec "admin.nodeInfo.enode"
        p = Popen([settings.GETH,
                   'attach', self.data_dir() + 'geth.ipc',
                   '--exec', 'admin.nodeInfo.enode'],
                  stdout=PIPE)
        enode = ''.join([line.decode('utf8') for line in p.stdout]).replace('"', '').replace('\n', '')
        p.wait()
        return enode

    def update_enode(self):
        self.enode = self.get_enode()
        self.save()
