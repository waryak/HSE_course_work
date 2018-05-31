import requests

from bms.celery import app


@app.task(name='run_command')
def run_command(command):
    print(command)


@app.task(name='init')
def init(node_id):
    from blockchain.models.node import Node
    node = Node.objects.get(id=node_id)
    node.init()


@app.task(name='connect')
def connect(node_id):
    from blockchain.models.node import Node
    node = Node.objects.get(id=node_id)
    node.connect()


@app.task(name='execute_code')
def execute_code(code):
    execute_url = 'http://localhost:1337/execute/'
    r = requests.get(execute_url, params={'code': code})
    return r.text

