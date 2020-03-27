#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import sys
import os
from PIL import Image, ImageColor
from duotone import Duotone


@click.command()
@click.option('--input', '-i', type=str, required=True, help='The input image file')
@click.option('--light_color', '-l', type=str, required=True, help='The hex color for the light areas')
@click.option('--dark_color', '-d', type=str, required=True, help='The hex color for the dark areas')
@click.option('--contrast', '-c', type=float, default=0.5, required=False, help='The shadow threshold [0.0 - 1.0]')
@click.option('--out', '-o', type=str, required=True, help='The output file')
def cli(input, light_color, dark_color, contrast, out):
    light_values = ImageColor.getrgb(light_color)
    dark_values = ImageColor.getrgb(dark_color)
    im = Image.open(input)
    result = Duotone.process(im, light_values, dark_values, contrast)

    result.save(out, 'PNG')


if __name__ == "__main__":
    sys.exit(cli())
