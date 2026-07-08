use crate::core::point3d::Point3D;
use crate::core::vector3d::Vector3D;

#[derive(Debug)]
pub struct OffsetTrayectoria {
    pub puntos: Vec<Point3D>,
}

impl OffsetTrayectoria {
    pub fn generar(
        puntos: &Vec<Point3D>,
        offset: f32,
        normal_plano: Vector3D
    ) -> Self {

        let n = normal_plano.normalize();
        let mut puntos_offset = Vec::new();

        for i in 0..puntos.len() {
            let p = puntos[i];

            // Desplazamiento perpendicular al plano
            let o = Point3D::new(
                p.x + n.x * offset,
                p.y + n.y * offset,
                p.z + n.z * offset,
            );

            puntos_offset.push(o);
        }

        Self { puntos: puntos_offset }
    }
}
