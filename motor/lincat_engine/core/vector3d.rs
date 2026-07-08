use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug, Clone, Copy)]
pub struct Vector3D {
    pub x: f32,
    pub y: f32,
    pub z: f32,
}

impl Vector3D {
    pub fn new(x: f32, y: f32, z: f32) -> Self {
        Self { x, y, z }
    }
}
pub fn sub(&self, other: &Vector3D) -> Vector3D {
    Vector3D::new(self.x - other.x, self.y - other.y, self.z - other.z)
}

pub fn magnitude(&self) -> f32 {
    (self.x*self.x + self.y*self.y + self.z*self.z).sqrt()
}

pub fn normalize(&self) -> Vector3D {
    let mag = self.magnitude();
    if mag == 0.0 {
        return Vector3D::new(0.0, 0.0, 0.0);
    }
    Vector3D::new(self.x / mag, self.y / mag, self.z / mag)
}
