#!/usr/bin/env python3

import solid
import numpy as np

BIG = 10000
epsilon = 1/BIG
resolution = 256

H = 230.9+93.1+13.9-16.6  # Distance between spheres

Dmin = 2*16.6
Dmax = 140.7
theta = np.arctan((H)/((Dmax-Dmin)/2))*180/np.pi

Dbase = 133.7
Hbase = 43.2

Dhollow = 68.2
Hhollow = 150

upper_plane = solid.cube(BIG, center=True)
upper_plane = solid.translate([0,0,BIG/2])(upper_plane)

ball_min = solid.sphere(d=Dmin,segments=resolution)
ball_min = solid.translate([0,0,H])(ball_min)
ball_max = solid.sphere(d=Dmax,segments=resolution)
nosecone = solid.hull()(ball_min, ball_max)
nosecone = solid.rotate([0,90-theta,0])(nosecone)
nosecone = solid.intersection()(upper_plane, nosecone)
base = solid.cylinder(d=Dbase, h=Hbase+epsilon,segments=resolution)
base = solid.translate([0,0,-Hbase])(base)

hollow = solid.cylinder(d=Dhollow, h=Hhollow*2, center=True, segments=resolution)
hollow = solid.translate([20,0,0])(hollow)

total = solid.union()(
            base,
            nosecone,
            )
total -= hollow

print(solid.scad_render(total))
