from django.db import models


class Blockchain(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='название'
    )

    class Meta:
        verbose_name = 'блокчейн'
        verbose_name_plural = 'блокчейны'

    def __str__(self):
        return self.title

    def run_command(self, node, command):
        node.run_command(command)

    def execute_code(self, node, code):
        node.execute_code(code)

    def roll_back(self):
        for node in self.node_set.all():
            # TODO
            node.run_command('ROLLBACK_COMMAND')

    def run_nodes(self):
        for node in self.node_set.all():
            # TODO
            node.run_command('RUN_COMMAND')
