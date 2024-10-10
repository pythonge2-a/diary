import click 
from . import add

@click.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def main(a,b):
    print(add(a,b))

main()
