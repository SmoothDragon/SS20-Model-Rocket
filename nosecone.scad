

difference() {
	union() {
		translate(v = [0, 0, -43.2000000000]) {
			cylinder($fn = 256, d = 133.7000000000, h = 43.2001000000);
		}
		intersection() {
			translate(v = [0, 0, 5000.0000000000]) {
				cube(center = true, size = 10000);
			}
			rotate(a = [0, 9.497019756414886, 0]) {
				hull() {
					translate(v = [0, 0, 321.3000000000]) {
						sphere($fn = 256, d = 33.2000000000);
					}
					sphere($fn = 256, d = 140.7000000000);
				}
			}
		}
	}
	translate(v = [20, 0, 0]) {
		cylinder($fn = 256, center = true, d = 68.2000000000, h = 300);
	}
}
