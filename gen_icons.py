# -*- coding: utf-8 -*-
"""生成 App 图标：绿底 + 象牙色麻将牌 + 红"胡"字"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.dirname(os.path.abspath(__file__))
FONT = 'C:/Windows/Fonts/simhei.ttf'

GREEN = (12, 66, 49)
IVORY = (250, 247, 238)
EDGE = (214, 204, 182)
RED = (192, 57, 47)

def make(size):
    img = Image.new('RGB', (size, size), GREEN)
    d = ImageDraw.Draw(img)
    m = size * 0.13
    r = size * 0.18
    # 牌身
    d.rounded_rectangle([m, m, size - m, size - m], radius=r, fill=IVORY, outline=EDGE, width=max(2, size // 96))
    # 内沿
    m2 = m + size * 0.035
    d.rounded_rectangle([m2, m2, size - m2, size - m2], radius=r * 0.82, outline=(228, 219, 198), width=max(1, size // 170))
    # "胡"
    f = ImageFont.truetype(FONT, int(size * 0.44))
    txt = '胡'
    bb = d.textbbox((0, 0), txt, font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    d.text(((size - w) / 2 - bb[0], (size - h) / 2 - bb[1] - size * 0.015), txt, font=f, fill=RED)
    return img

for s in (180, 192, 512):
    p = os.path.join(OUT, f'icon-{s}.png')
    make(s).save(p, 'PNG', optimize=True)
    print('ok', p, os.path.getsize(p))
