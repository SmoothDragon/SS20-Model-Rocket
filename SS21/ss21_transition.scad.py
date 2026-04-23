#!/usr/bin/env python3

import solidpython as sd
import numpy as np

BIG = 10000
epsilon = 1/BIG
resolution = 256


d_top = 11
d_base = 23.95
d_hole = 10.42
h_part = 23.3

upper_plane = sd.cube(BIG, center=True)
upper_plane = sd.translate([0,0,BIG/2])(upper_plane)

taper = sd.cylinder(d1=d_base, d2=d_top, h=h_part, segments=resolution)
hole = sd.cylinder(d=d_hole, h=h_part+2*epsilon,segments=resolution)
hole = sd.translate([0,0,-epsilon])(hole)

total = taper - hole

print(sd.scad_render(total))
