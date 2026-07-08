use crate::core::point3d::Point3D;
use std::f32::consts::PI;

#[derive(Debug)]
pub struct TrayectoriaHelicoidal {
    pub puntos: Vec<Point3D>,
}

impl TrayectoriaHelicoidal {
    pub fn generar(
        centro: Point3D,
        radio: f32,
        z_inicio: f32,
        z_fin: f32,
        vueltas: f32,
        pasos: usize,
        sentido_ccw: bool
    ) -> Self {

        let mut puntos = Vec::new();
        let pasos_totales = pasos * (vueltas as usize);
        let pitch = (z_fin - z_inicio) / vueltas;

        for i in 0..=pasos_totales {
            let t = i as f32 / pasos_totales as f32;
            let ang = t * vueltas * 2.0 * PI;

            let ang_final = if sentido_ccw { ang } else { -ang };

            let x = centro.x + radio * ang_final.cos();
            let y = centro.y + radio * ang_final.sin();
            let z = z_inicio + pitch * (ang / (2.0 * PI));

            puntos.push(Point3D::new(x, y, z));
        }

        Self { puntos }
    }
}
