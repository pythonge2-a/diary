import click
import time 

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")
    with click.progressbar([1, 2, 3]) as bar:
        for x in bar:
            print(f"sleep({x})...")
            time.sleep(x)
            
if __name__ == '__main__':
    hello()
