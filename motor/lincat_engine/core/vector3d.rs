#[derive(Serialize, Deserialize, Debug, Clone, Copy)]
pub struct Vector3D {
    pub x: f32,
    pub y: f32,
    pub z: f32,
}

impl Vector3D {
    #[inline]
    pub fn new(x: f32, y: f32, z: f32) -> Self {
        Self { x, y, z }
    }

    #[inline]
    pub fn sub(self, other: Self) -> Self {
        Self::new(self.x - other.x, self.y - other.y, self.z - other.z)
    }

    #[inline]
    pub fn magnitude(self) -> f32 {
        (self.x * self.x + self.y * self.y + self.z * self.z).sqrt()
    }

    #[inline]
    pub fn normalize(self) -> Self {
        let mag = self.magnitude();
        if mag < 1e-6 {
            Self::new(0.0, 0.0, 0.0)
        } else {
            Self::new(self.x / mag, self.y / mag, self.z / mag)
        }
    }
}
