import click
from models.http_disk_log_app import HttpDiskLogApp
# from models.http_kv_app import HttpKvApp


@click.command()
@click.option('--address', default="0.0.0.0", help='Server address')
@click.option('--port', default=8001, help='Server port')
def hello(**kwargs):
    http_handler_app = HttpDiskLogApp(**kwargs)
    http_handler_app.perform()

if __name__ == '__main__':
    hello()
