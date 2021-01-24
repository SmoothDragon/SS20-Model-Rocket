#!/usr/bin/env python3

import solid
import numpy as np

BIG = 10000
epsilon = 1/BIG
resolution = 256

# H = 7*25.4
H = 203.2

# Rocket main body
OD = 7.672*25.4
ID = 7.4*25.4
id_insert = 2*25.4

# Dmin = 1*25.4
Dmin = 3
# Dmax = 2*3.75*25.4
Dmax = OD
theta = 20*np.pi/180

trans = 5  # Transition height

R_carve = 3*25.4
R_carve = 140.7/2
shift = .6*25.4

upper_plane = solid.cube(BIG, center=True)
upper_plane = solid.translate([0,0,BIG/2])(upper_plane)

block = solid.cylinder(d1=Dmax, d2=Dmin, h=H-trans, segments=resolution)
block = solid.translate([0,0,trans])(block)
block += solid.cylinder(d=Dmax, h=trans, segments=resolution)
lower = solid.cylinder(d=ID, h=id_insert+epsilon, segments=resolution)
lower = solid.translate([0,0,-id_insert])(lower)
block += lower

block = solid.sphere(d=Dmax, segments=resolution)
block = solid.scale([1,1,2])(block)
block = solid.intersection()(block, upper_plane)

carve = solid.cylinder(r=R_carve, h=3*H, center=True, segments=resolution)
carve = solid.hull()(
            carve,
            solid.translate([BIG*np.cos(theta), BIG*np.sin(theta),0])(carve),
            solid.translate([BIG*np.cos(theta),-BIG*np.sin(theta),0])(carve),
            )
carve = solid.translate([R_carve+shift,0,0])(carve)
carve = solid.union()(
                carve,
                solid.rotate([0,0,120])(carve),
                solid.rotate([0,0,240])(carve),
                     )

total = solid.union()(
            block,
            )
total -= carve

print(solid.scad_render(total))
