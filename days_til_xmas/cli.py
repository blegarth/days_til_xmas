# -*- coding: utf-8 -*-

"""Console script for days_til_xmas."""
import sys
import click
import arrow


@click.command()
@click.argument('year', metavar='year')
def main(year):
    """An example command to show how many days until Xmas during a specific year"""
    if not year.isnumeric():
        click.echo('This command expects a numeric argument')
    else:
        x = (arrow.get(int(year), 12, 25) - arrow.utcnow()).days
        until = x if x > 0 else 'The date has passed'
        click.echo(until)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
