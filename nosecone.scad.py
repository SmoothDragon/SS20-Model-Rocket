#!/usr/bin/env python3

import solid
import numpy as np

H3 = 230.9
Dmin3 = 63.8
Dmax3 = 140.7
BIG = 10*H3
theta = np.arctan(1/6)*180/np.pi

cone3 = solid.cylinder(d1=Dmax3, d2=Dmin3, h=H3)
cone3 -= solid.cylinder(d=63.5, h=3*H3, center=True)
cone3 -= solid.cylinder(d=68.2, h=2*(H3-63.5), center=True)

upper_plane = solid.cube(BIG, center=True)
lower_plane = solid.translate([0,0,-BIG/2])(upper_plane)
upper_plane = solid.translate([0,0,BIG/2])(upper_plane)
cut_plane = solid.rotate([0, -theta, 0])(upper_plane)
cut_plane = solid.translate([Dmax3/2, 0, 0])(cut_plane)

bulb = solid.sphere(d=Dmax3)
bulb = solid.intersection()(upper_plane,bulb)
# bulb = solid.intersection()(bulb, cut_plane)
bulb_base = solid.cylinder(d=136.7, h=2*43.2, center=True)
bulb_base += bulb
bulb_base -= solid.cylinder(d=136.7/2, h=4*43.2, center=True)
bulb_base = solid.translate([-Dmax3/2, 0, 0])(bulb_base)
bulb_base = solid.rotate([0, -theta, 0])(bulb_base)
bulb_base = solid.translate([Dmax3/2, 0, 0])(bulb_base)
# bulb += bulb_base
bulb = solid.intersection()(bulb_base, lower_plane)

total = solid.union()(
            cone3,
            bulb,
            )

print(solid.scad_render(total))
