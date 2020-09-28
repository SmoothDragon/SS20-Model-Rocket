#!/usr/bin/env python3

import solid
import numpy as np

H3 = 230.9
Dmin3 = 63.8
Dmax3 = 140.7
BIG = 10*H3
theta = np.arctan(1/6)*180/np.pi

center_height = 230.9+93.1+13.9-16.6  # Height minus cap radius
top_r = 16.6
big_r = Dmax3/2
shell = 6  # thickness of shell

ball1 = solid.sphere(r=top_r)
ball1 = solid.translate([0,0,center_height])(ball1)
ball2 = solid.sphere(r=big_r)
cone = solid.hull()(ball1, ball2)
iball1 = solid.sphere(r=top_r-shell)
iball1 = solid.translate([0,0,center_height])(iball1)
iball2 = solid.sphere(r=big_r-shell-2)
icone = solid.hull()(iball1, iball2)

cone = cone - icone
# cone = solid.translate([-Dmax3/2, 0, 0])(cone)
cone = solid.rotate([0, theta, 0])(cone)
# cone = solid.translate([Dmax3/2, 0, 0])(cone)

upper_plane = solid.cube(BIG, center=True)
lower_plane = solid.translate([0,0,-BIG/2])(upper_plane)
upper_plane = solid.translate([0,0,BIG/2])(upper_plane)
cut_plane = solid.rotate([0, -theta, 0])(upper_plane)
cut_plane = solid.translate([Dmax3/2, 0, 0])(cut_plane)


cone = solid.intersection()(upper_plane,cone)
base = solid.cylinder(d=136.7, h=2*43.2, center=True)
base -= solid.cylinder(d=136.7-2*shell, h=3*43.2, center=True)
# base = solid.translate([1,0,0])(base)
base = solid.intersection()(base, lower_plane)

cone += base
bulb = cone
bulb = solid.intersection()(bulb, cut_plane)
bulb_base = solid.cylinder(d=136.7, h=2*43.2, center=True)
bulb_base += bulb
bulb_base -= solid.cylinder(d=136.7/2, h=4*43.2, center=True)
bulb_base = solid.translate([-Dmax3/2, 0, 0])(bulb_base)
bulb_base = solid.rotate([0, -theta, 0])(bulb_base)
bulb_base = solid.translate([Dmax3/2, 0, 0])(bulb_base)
# bulb += bulb_base
bulb = solid.intersection()(bulb_base, lower_plane)

total = solid.union()(
            cone,
            # bulb,
            )

print(solid.scad_render(total))
