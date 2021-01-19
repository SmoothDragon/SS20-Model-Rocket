

difference() {
	union() {
		union() {
			translate(v = [0, 0, 5]) {
				cylinder($fn = 256, d1 = 194.8688000000, d2 = 3, h = 198.2000000000);
			}
			cylinder($fn = 256, d = 194.8688000000, h = 5);
			translate(v = [0, 0, -50.8000000000]) {
				cylinder($fn = 256, d = 187.9600000000, h = 50.8001000000);
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
