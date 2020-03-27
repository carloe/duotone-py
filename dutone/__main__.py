#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import sys


@click.command()
def cli():
    print("Hello World")


if __name__ == "__main__":
    sys.exit(cli())