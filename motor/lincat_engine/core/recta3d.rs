use serde::{Serialize, Deserialize};
use crate::core::point3d::Point3D;
use crate::core::vector3d::Vector3D;

#[derive(Serialize, Deserialize, Debug, Clone, Copy)]
pub struct Recta3D {
    pub punto: Point3D,
    pub direccion: Vector3D,
}

impl Recta3D {
    pub fn new(punto: Point3D, direccion: Vector3D) -> Self {
        Self {
            punto,
            direccion: direccion.normalize(),
        }
    }

    pub fn punto_en_t(&self, t: f32) -> Point3D {
        Point3D::new(
            self.punto.x + self.direccion.x * t,
            self.punto.y + self.direccion.y * t,
            self.punto.z + self.direccion.z * t,
        )
    }

    pub fn distancia_a_punto(&self, p: &Point3D) -> f32 {
        let ap = Vector3D::new(
            p.x - self.punto.x,
            p.y - self.punto.y,
            p.z - self.punto.z,
        );

        let proy = ap.dot(&self.direccion);
        let punto_proy = self.punto_en_t(proy);

        let dx = p.x - punto_proy.x;
        let dy = p.y - punto_proy.y;
        let dz = p.z - punto_proy.z;

        (dx*dx + dy*dy + dz*dz).sqrt()
    }
}
