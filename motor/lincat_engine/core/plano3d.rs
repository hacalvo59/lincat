use serde::{Serialize, Deserialize};
use crate::core::vector3d::Vector3D;

#[derive(Serialize, Deserialize, Debug, Clone, Copy)]
pub struct Plano3D {
    pub punto: Vector3D,
    pub normal: Vector3D,
}

impl Plano3D {
    #[inline]
    pub fn new(punto: Vector3D, normal: Vector3D) -> Self {
        Self {
            punto,
            normal: normal.normalize(),
        }
    }

    #[inline]
    pub fn distancia_al_punto(self, p: Vector3D) -> f32 {
        let v = p.sub(self.punto);
        v.dot(self.normal)
    }

    #[inline]
    pub fn proyectar_punto(self, p: Vector3D) -> Vector3D {
        let d = self.distancia_al_punto(p);
        Vector3D::new(
            p.x - self.normal.x * d,
            p.y - self.normal.y * d,
            p.z - self.normal.z * d,
        )
    }
}
