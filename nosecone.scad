

union() {
	difference() {
		difference() {
			cylinder(d1 = 140.7000000000, d2 = 63.8000000000, h = 230.9000000000);
			cylinder(center = true, d = 63.5000000000, h = 692.7000000000);
		}
		cylinder(center = true, d = 68.2000000000, h = 334.8000000000);
	}
	intersection() {
		union() {
			intersection() {
				difference() {
					sphere(d = 140.7000000000);
					translate(v = [0, 0, 1154.5000000000]) {
						cube(center = true, size = 2309.0000000000);
					}
				}
				translate(v = [70.3500000000, 0, 0]) {
					rotate(a = [0, -9.462322208025617, 0]) {
						translate(v = [0, 0, 1154.5000000000]) {
							cube(center = true, size = 2309.0000000000);
						}
					}
				}
			}
			translate(v = [70.3500000000, 0, 0]) {
				rotate(a = [0, -9.462322208025617, 0]) {
					translate(v = [-70.3500000000, 0, 0]) {
						cylinder(center = true, d = 136.7000000000, h = 86.4000000000);
					}
				}
			}
		}
		translate(v = [0, 0, -1154.5000000000]) {
			cube(center = true, size = 2309.0000000000);
		}
	}
}
