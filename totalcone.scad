

union() {
	union() {
		intersection() {
			translate(v = [0, 0, 1154.5000000000]) {
				cube(center = true, size = 2309.0000000000);
			}
			rotate(a = [0, 9.462322208025617, 0]) {
				difference() {
					hull() {
						translate(v = [0, 0, 321.3000000000]) {
							sphere(r = 16.6000000000);
						}
						sphere(r = 70.3500000000);
					}
					hull() {
						translate(v = [0, 0, 321.3000000000]) {
							sphere(r = 10.6000000000);
						}
						sphere(r = 62.3500000000);
					}
				}
			}
		}
		intersection() {
			difference() {
				cylinder(center = true, d = 136.7000000000, h = 86.4000000000);
				cylinder(center = true, d = 124.7000000000, h = 129.6000000000);
			}
			translate(v = [0, 0, -1154.5000000000]) {
				cube(center = true, size = 2309.0000000000);
			}
		}
	}
}
