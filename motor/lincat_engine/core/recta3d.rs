use serde::{Serialize, Deserialize};
use crate::core::vector3d::Vector3D;

#[derive(Serialize, Deserialize, Debug, Clone, Copy)]
pub struct Recta3D {
    pub punto: Vector3D,
    pub direccion: Vector3D,
}

impl Recta3D {
    #[inline]
    pub fn new(punto: Vector3D, direccion: Vector3D) -> Self {
        Self {
            punto,
            direccion: direccion.normalize(),
        }
    }

    #[inline]
    pub fn punto_en_t(self, t: f32) -> Vector3D {
        Vector3D::new(
            self.punto.x + self.direccion.x * t,
            self.punto.y + self.direccion.y * t,
            self.punto.z + self.direccion.z * t,
        )
    }

    #[inline]
    pub fn distancia_a_punto(self, p: Vector3D) -> f32 {
        let ap = p.sub(self.punto);
        let proy = ap.dot(self.direccion);
        let punto_proy = self.punto_en_t(proy);
        p.sub(punto_proy).magnitude()
    }
}
