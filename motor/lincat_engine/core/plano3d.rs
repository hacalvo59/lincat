use serde::{Serialize, Deserialize};
use crate::core::point3d::Point3D;
use crate::core::vector3d::Vector3D;

#[derive(Serialize, Deserialize, Debug, Clone, Copy)]
pub struct Plano3D {
    pub punto: Point3D,
    pub normal: Vector3D,
}

impl Plano3D {
    pub fn new(punto: Point3D, normal: Vector3D) -> Self {
        Self { punto, normal: normal.normalize() }
    }

    pub fn distancia_al_punto(&self, p: &Point3D) -> f32 {
        let v = Vector3D::new(
            p.x - self.punto.x,
            p.y - self.punto.y,
            p.z - self.punto.z,
        );
        self.normal.dot(&v)
    }
}
