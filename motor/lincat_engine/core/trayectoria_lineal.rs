use crate::core::point3d::Point3D;
use crate::core::vector3d::Vector3D;
use crate::core::recta3d::Recta3D;

#[derive(Debug)]
pub struct TrayectoriaLineal {
    pub puntos: Vec<Point3D>,
}

impl TrayectoriaLineal {
    pub fn generar(p_inicio: Point3D, p_fin: Point3D, pasos: usize) -> Self {
        let dir = Vector3D::new(
            p_fin.x - p_inicio.x,
            p_fin.y - p_inicio.y,
            p_fin.z - p_inicio.z,
        );

        let recta = Recta3D::new(p_inicio, dir);

        let mut puntos = Vec::new();
        let pasos_f = pasos as f32;

        for i in 0..=pasos {
            let t = i as f32 / pasos_f;
            puntos.push(recta.punto_en_t(t));
        }

        Self { puntos }
    }
}
