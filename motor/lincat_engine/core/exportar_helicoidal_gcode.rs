use crate::core::point3d::Point3D;

pub struct ExportadorHelicoidalGcode;

impl ExportadorHelicoidalGcode {
    pub fn desde_trayectoria(
        puntos: &Vec<Point3D>,
        feedrate: f32,
        usar_mm: bool,
        sentido_ccw: bool,
        centro_x: f32,
        centro_y: f32
    ) -> String {

        let mut gcode = String::new();

        // Unidades
        if usar_mm {
            gcode.push_str("G21\n");
        } else {
            gcode.push_str("G20\n");
        }

        // Modo absoluto
        gcode.push_str("G90\n");

        if puntos.len() < 2 {
            gcode.push_str("M2\n");
            return gcode;
        }

        // Primer punto: posicionamiento rápido
        let p0 = puntos[0];
        gcode.push_str(&format!("G0 X{:.3} Y{:.3} Z{:.3}\n", p0.x, p0.y, p0.z));

        // Feedrate
        gcode.push_str(&format!("F{:.1}\n", feedrate));

        // Último punto de la hélice
        let p_last = puntos[puntos.len() - 1];

        // Centro relativo I, J
        let i = centro_x - p0.x;
        let j = centro_y - p0.y;

        // Sentido
        let g = if sentido_ccw { "G3" } else { "G2" };

        // Movimiento helicoidal: arco + Z final
        gcode.push_str(&format!(
            "{g} X{:.3} Y{:.3} Z{:.3} I{:.3} J{:.3}\n",
            p_last.x, p_last.y, p_last.z, i, j
        ));

        gcode.push_str("M2\n");

        gcode
    }
}
