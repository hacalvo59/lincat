use serde::{Serialize, Deserialize};
use crate::core::vector3d::Vector3D;

#[derive(Serialize, Deserialize, Debug, Clone, Copy)]
pub struct Arco3D {
    pub centro: Vector3D,
    pub radio: f32,
    pub normal: Vector3D,
    pub inicio: Vector3D,
    pub fin: Vector3D,
}

impl Arco3D {
    #[inline]
    pub fn new(centro: Vector3D, inicio: Vector3D, fin: Vector3D, normal: Vector3D) -> Self {
        let radio = inicio.sub(centro).magnitude();
        Self {
            centro,
            radio,
            normal: normal.normalize(),
            inicio,
            fin,
        }
    }

    #[inline]
    pub fn punto_en_angulo(self, ang: f32) -> Vector3D {
        let dir0 = self.inicio.sub(self.centro).normalize();
        let dir1 = self.normal.cross(dir0).normalize();

        let x = dir0.x * ang.cos() + dir1.x * ang.sin();
        let y = dir0.y * ang.cos() + dir1.y * ang.sin();
        let z = dir0.z * ang.cos() + dir1.z * ang.sin();

        Vector3D::new(
            self.centro.x + x * self.radio,
            self.centro.y + y * self.radio,
            self.centro.z + z * self.radio,
        )
    }

    #[inline]
    pub fn angulo_total(self) -> f32 {
        let v0 = self.inicio.sub(self.centro).normalize();
        let v1 = self.fin.sub(self.centro).normalize();
        let dot = v0.dot(v1).clamp(-1.0, 1.0);
        dot.acos()
    }
}
