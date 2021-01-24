

difference() {
	union() {
		translate(v = [0, 0, -43.2000000000]) {
			cylinder($fn = 256, d = 133.7000000000, h = 43.2001000000);
		}
		intersection() {
			translate(v = [0, 0, 5000.0000000000]) {
				cube(center = true, size = 10000);
			}
			union() {
				translate(v = [71.3500000000, 0, 0]) {
					rotate(a = [0, 9.67040160015732, 0]) {
						translate(v = [-71.3500000000, 0, 0]) {
							difference() {
								union() {
									intersection() {
										cylinder($fn = 256, d1 = 140.7000000000, d2 = 10140.7000000000, h = 10000);
										hull() {
											translate(v = [0, 0, 321.3000000000]) {
												sphere($fn = 256, d = 33.2000000000);
											}
											sphere($fn = 256, d = 142.7000000000);
										}
									}
									translate(v = [-60, 0, 24]) {
										rotate(a = [0, 9.67040160015732, 0]) {
											hull() {
												cube(center = true, size = [17, 2.5000000000, 13.6000000000]);
												cube(center = true, size = [24.2000000000, 2, 10]);
											}
										}
									}
								}
								translate(v = [0, 0, 299.3000000000]) {
									rotate_extrude(angle = 360) {
										translate(v = [22, 0, 0]) {
											circle(r = 2);
										}
									}
								}
							}
						}
					}
				}
				sphere($fn = 256, d = 140.7000000000);
			}
		}
	}
	translate(v = [25, 0, 0]) {
		cylinder($fn = 256, center = true, d = 68.2000000000, h = 300);
	}
	translate(v = [-25, 0, 0]) {
		cylinder($fn = 256, center = true, d = 38.1000000000, h = 254.0000000000);
	}
	translate(v = [0, 0, -43.2000000000]) {
		sphere($fn = 256, d = 123.7000000000);
	}
}
