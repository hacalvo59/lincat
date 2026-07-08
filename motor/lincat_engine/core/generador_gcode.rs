use crate::core::point3d::Point3D;

pub struct GeneradorGcode;

impl GeneradorGcode {

    pub fn desde_trayectoria(
        puntos: &Vec<Point3D>,
        feedrate: f32,
        usar_mm: bool,
        modo_relativo: bool
    ) -> String {

        let mut gcode = String::new();

        // Unidades
        if usar_mm {
            gcode.push_str("G21\n");
        } else {
            gcode.push_str("G20\n");
        }

        // Modo absoluto o relativo
        if modo_relativo {
            gcode.push_str("G91\n");
        } else {
            gcode.push_str("G90\n");
        }

        if puntos.is_empty() {
            gcode.push_str("M2\n");
            return gcode;
        }

        // Primer punto: movimiento rápido
        let p0 = puntos[0];
        gcode.push_str(&format!("G0 X{:.3} Y{:.3} Z{:.3}\n", p0.x, p0.y, p0.z));

        // Feedrate
        gcode.push_str(&format!("F{:.1}\n", feedrate));

        // Resto de puntos
        let mut prev = p0;

        for p in puntos.iter().skip(1) {
            if modo_relativo {
                // ΔX ΔY ΔZ
                let dx = p.x - prev.x;
                let dy = p.y - prev.y;
                let dz = p.z - prev.z;

                gcode.push_str(&format!("G1 X{:.3} Y{:.3} Z{:.3}\n", dx, dy, dz));
            } else {
                // Absoluto
                gcode.push_str(&format!("G1 X{:.3} Y{:.3} Z{:.3}\n", p.x, p.y, p.z));
            }

            prev = *p;
        }

        gcode.push_str("M2\n");

        gcode
    }
}
