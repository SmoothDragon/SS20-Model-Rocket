#!/usr/bin/env python3

'''
Make first grid fin for SS20 rocket.


'''

from solid import *
from solid.utils import *

gridBoxX = 121.4
gridBoxY = 134.9

def grid(fin_width, fin_spacing, fin_height, n:'iterations'):
    limit = fin_spacing * 2**(n+1)
    slat = cube([fin_width, limit, fin_height], center=True)
    slats = slat + rotate([0,0,90])(slat)
    for i in range(n):
        shift = (-2)**(i) * fin_spacing
        slats = union()(slats, translate([shift, shift, 0])(slats))
    return slats

def gridFinOne(grid, strut_width, strut_height, strut_length, crossRail_length):
    miniGridY = 1.0375*25.4
    gridY = (4.75-1.0375-1.125)
    strut_Yshift = 25.4 * (2.5-(gridY/2+1.125))
    gridY *= 25.4
    block = cube([crossRail_length, gridY, strut_height], center=True)
    extension = cube([1.05*25.4, miniGridY, strut_height], center=True)
    ext_top = cube([crossRail_length, strut_width, strut_height], center=True)
    block += translate([(crossRail_length-1.05*25.4)/2, (gridY+miniGridY)/2, 0])(extension)
    block += translate([-(crossRail_length-1.05*25.4)/2, (gridY+miniGridY)/2, 0])(extension)
    ext_top = translate([0, (gridY-strut_width)/2+miniGridY, 0])(ext_top)
    ext_top = intersection()(ext_top, block)
    grid = rotate([0,0,45])(grid)
    block = intersection()(block, grid)
    block += ext_top
    ext_side = cube([strut_width, miniGridY, strut_height], center=True)
    block += translate([25.4*.9/2, gridY/2+miniGridY/2,0])(ext_side)
    block += translate([-25.4*.9/2, gridY/2+miniGridY/2,0])(ext_side)
    strut = cube([strut_width, strut_length, strut_height], center=True)
    strut = cube([crossRail_length, strut_width, strut_height], center=True)
    block = union()(block, translate([0, (gridY-strut_width)/2, 0])(strut))
    block = union()(block, translate([0, -(gridY-strut_width)/2, 0])(strut))
    points = [(0,0), (0,.3), (.3,.5), (4.75,.5), (4.75,.1), (1.125,.1), (1.125,0)]
    points = [(25.4*x, 25.4*y) for x,y in points]
    side = polygon(points=points)
    hole = circle(d=25.4*11/64)
    hole = translate([.4375*25.4,.25*25.4])(hole)
    side = side - hole
    side = linear_extrude(height=strut_width, center=True, convexity=10)(side)
    side = rotate([90, 0, 90])(side)
    side = translate([0, -gridY/2-25.4*1.125, -(.25+.05)*25.4])(side)
    block = union()(block, translate([(crossRail_length-strut_width)/2, 0, 0])(side))
    block = union()(block, translate([-(crossRail_length-strut_width)/2, 0, 0])(side))
    block = rotate([0,180,0])(block)
    # Add support angle
    support_x = .875 * 25.4
    support_y = .4375 * 25.4
    support = cube([support_x, strut_width, strut_height])
    support_shear = [
        [1,0,0,-crossRail_length/2],
        [support_y/support_x,1,0],
        [0,0,1,0],
        [0,0,0,1],
        ]
    support = multmatrix(m=support_shear)(support)
    support = translate([0,-gridY/2-support_y,-strut_height/2])(support)
    block += support
    block += rotate([0,180,0])(support)
    return block


if __name__ == '__main__':
    fin_spacing = 11
    fin_thickness = 1.2
    fin_height = 12.7
    strut_thickness = 3
    strut_height = 25.4 * .4
    strut_width = 25.4 * .093
    strut_length = 25.4 * 5
    side_strut_length = 25.4 * 2.9375
    boxY = 121.4
    boxX = 134.9

    box = cube([boxX, boxY, fin_height], center=True)

    fin = cube([fin_thickness, 2*boxY, fin_height], center=True)
    fins = union()(*[translate([i*fin_spacing,0,0])(fin) for i in range(-20,20)])
    fins += rotate([0,0,90])(fins)
    fins = rotate([0,0,45])(fins)


    # extGrid = grid(fin_thickness/2, fin_spacing, fin_height, 5)
    grid = intersection()(box, fins)
    sideX = cube([strut_thickness, boxY, fin_height], center=True)
    sideY = cube([boxX, strut_thickness, fin_height], center=True)

    main_fin = union()(fins,
            translate([(boxX-strut_thickness)/2,0,0])(sideX),
            translate([-(boxX-strut_thickness)/2,0,0])(sideX),
            translate([0,(boxY-strut_thickness)/2,0])(sideY),
            translate([0,-(boxY-strut_thickness)/2,0])(sideY),
            )
    main_fin = intersection()(main_fin, box)
    main_fin = translate([0,boxY/2,0])(main_fin)

    side_fin = cube([strut_thickness,12.7*2,fin_height], center=True)

    diag_strut = cube([strut_thickness, 26, fin_height])
    diag_strut = rotate([0,0,60])(diag_strut)
    diag_strut = translate([(boxX-2*strut_thickness)/2,-12.7,-fin_height/2])(diag_strut)
    flat_strut = cube([12.7, strut_thickness, fin_height], center=True)
    flat_strut = translate([41,-strut_thickness/2,0])(flat_strut)
    final = union()(main_fin,
            translate([(boxX-strut_thickness)/2,0,0])(side_fin),
            translate([-(boxX-strut_thickness)/2,0,0])(side_fin),
            diag_strut,
            rotate([0,180,0])(diag_strut),
            flat_strut,
            rotate([0,180,0])(flat_strut),
            )


    # print(scad_render(final, file_header=f'$fn={args.fn};'))
    fn = 64
    print(scad_render(final, file_header=f'$fn={fn};'))
