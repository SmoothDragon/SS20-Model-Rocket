

difference() {
	union() {
		intersection() {
			scale(v = [1, 1, 2]) {
				sphere($fn = 256, d = 194.8688000000);
			}
			translate(v = [0, 0, 5000.0000000000]) {
				cube(center = true, size = 10000);
			}
		}
	}
	union() {
		translate(v = [85.5900000000, 0, 0]) {
			hull() {
				cylinder($fn = 256, center = true, h = 609.6000000000, r = 70.3500000000);
				translate(v = [9396.926207859084, 3420.2014332566873, 0]) {
					cylinder($fn = 256, center = true, h = 609.6000000000, r = 70.3500000000);
				}
				translate(v = [9396.926207859084, -3420.2014332566873, 0]) {
					cylinder($fn = 256, center = true, h = 609.6000000000, r = 70.3500000000);
				}
			}
		}
		rotate(a = [0, 0, 120]) {
			translate(v = [85.5900000000, 0, 0]) {
				hull() {
					cylinder($fn = 256, center = true, h = 609.6000000000, r = 70.3500000000);
					translate(v = [9396.926207859084, 3420.2014332566873, 0]) {
						cylinder($fn = 256, center = true, h = 609.6000000000, r = 70.3500000000);
					}
					translate(v = [9396.926207859084, -3420.2014332566873, 0]) {
						cylinder($fn = 256, center = true, h = 609.6000000000, r = 70.3500000000);
					}
				}
			}
		}
		rotate(a = [0, 0, 240]) {
			translate(v = [85.5900000000, 0, 0]) {
				hull() {
					cylinder($fn = 256, center = true, h = 609.6000000000, r = 70.3500000000);
					translate(v = [9396.926207859084, 3420.2014332566873, 0]) {
						cylinder($fn = 256, center = true, h = 609.6000000000, r = 70.3500000000);
					}
					translate(v = [9396.926207859084, -3420.2014332566873, 0]) {
						cylinder($fn = 256, center = true, h = 609.6000000000, r = 70.3500000000);
					}
				}
			}
		}
	}
}
