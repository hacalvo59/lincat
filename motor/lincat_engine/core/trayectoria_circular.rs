use crate::core::point3d::Point3D;
use std::f32::consts::PI;

#[derive(Debug)]
pub struct TrayectoriaCircular {
    pub puntos: Vec<Point3D>,
}

impl TrayectoriaCircular {
    pub fn generar(
        inicio: Point3D,
        fin: Point3D,
        centro: Point3D,
        pasos: usize,
        sentido_ccw: bool
    ) -> Self {

        let mut puntos = Vec::new();

        let v_ini = (
            inicio.x - centro.x,
            inicio.y - centro.y,
            inicio.z - centro.z,
        );

        let v_fin = (
            fin.x - centro.x,
            fin.y - centro.y,
            fin.z - centro.z,
        );

        let ang_ini = v_ini.1.atan2(v_ini.0);
        let ang_fin = v_fin.1.atan2(v_fin.0);

        let mut delta = ang_fin - ang_ini;

        if sentido_ccw && delta < 0.0 {
            delta += 2.0 * PI;
        } else if !sentido_ccw && delta > 0.0 {
            delta -= 2.0 * PI;
        }

        let pasos_f = pasos as f32;

        for i in 0..=pasos {
            let t = i as f32 / pasos_f;
            let ang = ang_ini + delta * t;

            puntos.push(Point3D::new(
                centro.x + ang.cos() * v_ini.0.hypot(v_ini.1),
                centro.y + ang.sin() * v_ini.0.hypot(v_ini.1),
                centro.z
            ));
        }

        Self { puntos }
    }
}
