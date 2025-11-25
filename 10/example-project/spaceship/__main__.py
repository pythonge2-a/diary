import click 

from spaceship import convert_liter_to_gallon

@click.command()
@click.argument('liters', type=float)
def main(liters):
    """Convert LITERS to gallons and print the result."""
    gallons = convert_liter_to_gallon(liters)
    click.echo(f"{liters} liters is equal to {gallons:.2f} gallons.")

if __name__ == '__main__':
    main()