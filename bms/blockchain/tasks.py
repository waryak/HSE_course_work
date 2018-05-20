import requests

from bms.celery import app


@app.task(name='run_command')
def run_command(command):
    # TODO
    print(command)
    return 'success'


@app.task(name='execute_code')
def execute_code(code):
    execute_url = 'http://localhost:1337/execute/'
    r = requests.get(execute_url, params={'code': code})
    return r.text

