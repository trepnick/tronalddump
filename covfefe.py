#!/usr/bin/env python3

import requests
import click

TRONALD_DUMP_URL = "https://tronalddump.io"
CHUCK_NORRIS_URL = "https://api.chucknorris.io"
ADVICE_URL = "https://api.adviceslip.com"


@click.command()
@click.option("-t", is_flag=True)
@click.option("-c", is_flag=True)
@click.option("-a", is_flag=True)
def cli(t, c, a):
    if t:
        click.echo(get_random_trump_quote())
    elif c:
        click.echo(get_random_chuck_fact())
    elif a:
        click.echo(get_random_advice())
    else:
        click.echo(get_random_chuck_fact())


def get_random_trump_quote():
    r = requests.get(TRONALD_DUMP_URL + "/random/quote")
    return r.json()["value"]


def get_random_chuck_fact():
    r = requests.get(CHUCK_NORRIS_URL + "/jokes/random")
    return r.json()["value"]


def get_random_advice():
    r = requests.get(ADVICE_URL + "/advice")
    return r.json()["slip"]["advice"]


if __name__ == "__main__":
    cli()
