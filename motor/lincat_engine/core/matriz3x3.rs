use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug, Clone, Copy)]
pub struct Matriz3x3 {
    pub m: [[f32; 3]; 3],
}

impl Matriz3x3 {
    pub fn new(m: [[f32; 3]; 3]) -> Self {
        Self { m }
    }

    pub fn identidad() -> Self {
        Self {
            m: [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
            ]
        }
    }

    pub fn mul_vector(&self, v: crate::core::vector3d::Vector3D) -> crate::core::vector3d::Vector3D {
        let x = self.m[0][0]*v.x + self.m[0][1]*v.y + self.m[0][2]*v.z;
        let y = self.m[1][0]*v.x + self.m[1][1]*v.y + self.m[1][2]*v.z;
        let z = self.m[2][0]*v.x + self.m[2][1]*v.y + self.m[2][2]*v.z;
        crate::core::vector3d::Vector3D::new(x, y, z)
    }
}
