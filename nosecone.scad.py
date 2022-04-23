#!/usr/bin/env python3

import solid
import numpy as np

BIG = 10000
epsilon = 1/BIG
resolution = 256

H = 230.9+93.1+13.9-16.6  # Distance between spheres

Dmin = 2*16.6
Dbase = 140.7
rim = 2
Dmax = Dbase+rim
theta = np.arctan((H)/((Dmax-Dmin)/2))*180/np.pi

Dinsert = 133.7
Hinsert = 43.2

Dhollow = 68.2
Hhollow = 150

Dsmoke = 1.5*25.4
Hsmoke = 5*25.4

upper_plane = solid.cube(BIG, center=True)
upper_plane = solid.translate([0,0,BIG/2])(upper_plane)

ball_min = solid.sphere(d=Dmin,segments=resolution)
ball_min = solid.translate([0,0,H])(ball_min)
ball_max = solid.sphere(d=Dmax,segments=resolution)
nosecone = solid.hull()(ball_min, ball_max)
# nosecone = solid.intersection()(upper_plane, nosecone)
taper = solid.cylinder(d1=Dbase, d2=BIG+Dbase, h=BIG, segments=resolution)
nosecone = solid.intersection()(taper, nosecone)
minifin_top = solid.cube([17,2.5,10+3.6], center=True)
minifin_bot = solid.cube([17+7.2,2,10], center=True)
minifin = solid.hull()(minifin_top, minifin_bot)
minifin = solid.rotate([0,90-theta,0])(minifin)
minifin = solid.translate([-60,0,24])(minifin)
nosecone += minifin
nose_groove = solid.translate([22,0,0])(solid.circle(2))
nose_groove = solid.rotate_extrude()(nose_groove)
nose_groove = solid.translate([0,0,H-22])(nose_groove)
nosecone -= nose_groove
nosecone = solid.translate([-Dmax/2,0,0])(nosecone)
nosecone = solid.rotate([0,90-theta,0])(nosecone)
nosecone = solid.translate([Dmax/2,0,0])(nosecone)
nosecone += solid.sphere(d=Dbase,segments=resolution)
nosecone = solid.intersection()(upper_plane, nosecone)
insert = solid.cylinder(d=Dinsert, h=Hinsert+epsilon,segments=resolution)
insert = solid.translate([0,0,-Hinsert])(insert)

hollow = solid.cylinder(d=Dhollow, h=Hhollow*2, center=True, segments=resolution)
hollow = solid.translate([25,0,0])(hollow)
smoke = solid.cylinder(d=Dsmoke, h=Hsmoke*2, center=True, segments=resolution)
smoke = solid.translate([-25,0,0])(smoke)

open_bottom = solid.sphere(d=Dinsert-10, segments=resolution)
open_bottom = solid.translate([0,0,-Hinsert])(open_bottom)

total = solid.union()(
            insert,
            nosecone,
            )
total -= hollow
# total -= smoke
total -= open_bottom

print(solid.scad_render(total))
