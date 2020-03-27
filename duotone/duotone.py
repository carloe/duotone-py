# -*- coding: utf-8 -*-
from PIL import Image
import math


class Duotone:
    @staticmethod
    def process(im: Image, light_color: (int, int, int, int), dark_color: (int, int, int, int), contrast: float = 0.5):
        im = im.convert('RGB')
        out = Image.new(im.mode, im.size)
        out_pixels = out.load()

        do_calc_contrast = contrast != 0.5
        contrast_norm = (1 + contrast - 0.5)

        for i in range(im.size[0]):
            for j in range(im.size[1]):
                r, g, b = im.getpixel((i, j))

                if do_calc_contrast:
                    r = Duotone.__safe_color_value((r / 255.0 - 0.5) * contrast_norm + 0.5)
                    g = Duotone.__safe_color_value((g / 255.0 - 0.5) * contrast_norm + 0.5)
                    b = Duotone.__safe_color_value((b / 255.0 - 0.5) * contrast_norm + 0.5)
                average = math.floor(0.299 * r + 0.587 * g + 0.114 * b)
                h, s, l = Duotone.__rgb_to_hls(average, average, average)
                luminosity = max(0, min(254, math.floor(l * 254)))
                ratio = luminosity / 255.0
                new_r = math.floor(light_color[0] * ratio + dark_color[0] * (1 - ratio))
                new_g = math.floor(light_color[1] * ratio + dark_color[1] * (1 - ratio))
                new_b = math.floor(light_color[2] * ratio + dark_color[2] * (1 - ratio))
                out_pixels[i, j] = (new_r, new_g, new_b)
        return out

    @staticmethod
    def __safe_color_value(value):
        return min(255.0, max(0.0, value))

    @staticmethod
    def __rgb_to_hls(red, green, blue):
        red_norm = red / 255.0
        green_norm = green / 255.0
        blue_norm = blue / 255.0

        max_value = max(blue_norm, max(red_norm, green_norm))
        min_value = min(blue_norm, min(red_norm, green_norm))
        h = 0.0
        s = 0.0
        l = (max_value + min_value) / 2.0
        if max_value is not min_value:
            delta = max_value - min_value
            s = delta / (2 - max_value - min_value) if l > 0.5 else delta / (max_value + min_value)

            if max_value == red_norm:
                h = 6.0 if (green_norm - blue_norm) / delta + (green_norm < blue_norm) else 0.0
            if max_value == green_norm:
                h = (blue_norm - red_norm) / delta + 2.0
            if max_value == blue_norm:
                h = (red_norm - green_norm) / delta + 4.0
            h /= 6.0
        return h, s, l
