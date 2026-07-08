use serde::{Serialize, Deserialize};
use crate::core::vector3d::Vector3D;

#[derive(Serialize, Deserialize, Debug, Clone, Copy)]
pub struct Matriz3x3 {
    pub m: [[f32; 3]; 3],
}

impl Matriz3x3 {
    #[inline]
    pub fn new(m: [[f32; 3]; 3]) -> Self {
        Self { m }
    }

    #[inline]
    pub fn identidad() -> Self {
        Self {
            m: [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
            ]
        }
    }

    #[inline]
    pub fn mul_vector(self, v: Vector3D) -> Vector3D {
        Vector3D::new(
            self.m[0][0] * v.x + self.m[0][1] * v.y + self.m[0][2] * v.z,
            self.m[1][0] * v.x + self.m[1][1] * v.y + self.m[1][2] * v.z,
            self.m[2][0] * v.x + self.m[2][1] * v.y + self.m[2][2] * v.z,
        )
    }

    #[inline]
    pub fn mul(self, other: Self) -> Self {
        let mut r = [[0.0f32; 3]; 3];
        for i in 0..3 {
            for j in 0..3 {
                r[i][j] = self.m[i][0] * other.m[0][j]
                        + self.m[i][1] * other.m[1][j]
                        + self.m[i][2] * other.m[2][j];
            }
        }
        Self::new(r)
    }
}
