import click
from dotenv import load_dotenv

from models.stress_generator import StressGenerator

load_dotenv()


@click.command()
@click.option("--address",             default="localhost", help="Server address")
@click.option("--port",                default=8000,        help="Server port")
@click.option("--payload_size",        default=10,          help="Set the payload size")
@click.option("--qty_iteration",       default=10000,       help="Set the key range to determine the volume")
@click.option("--read_rate",           default=10,          help="Set the reading rate from 0 to 100 percent")
@click.option("--n_threads",           default=10,          help="Set number of client threads")
@click.option("--thinking_time",       default=0.1,         help="Set thinking time between requests")
@click.option("--percentage_sampling", default=50,          help="Percentage of log in total")
@click.option("--duration",            default=1,           help="Duration in seconds")
def hello(**kwargs):
    StressGenerator().perform(**kwargs)


if __name__ == '__main__':
    hello()
