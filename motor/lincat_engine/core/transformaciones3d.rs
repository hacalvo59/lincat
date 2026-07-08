use crate::core::matriz3x3::Matriz3x3;
use crate::core::vector3d::Vector3D;

pub struct Transformaciones3D;

impl Transformaciones3D {

    #[inline]
    pub fn rotacion_x(grados: f32) -> Matriz3x3 {
        let r = grados.to_radians();
        Matriz3x3::new([
            [1.0, 0.0,     0.0    ],
            [0.0, r.cos(), -r.sin()],
            [0.0, r.sin(),  r.cos()],
        ])
    }

    #[inline]
    pub fn rotacion_y(grados: f32) -> Matriz3x3 {
        let r = grados.to_radians();
        Matriz3x3::new([
            [ r.cos(), 0.0, r.sin()],
            [ 0.0,    1.0, 0.0    ],
            [-r.sin(), 0.0, r.cos()],
        ])
    }

    #[inline]
    pub fn rotacion_z(grados: f32) -> Matriz3x3 {
        let r = grados.to_radians();
        Matriz3x3::new([
            [r.cos(), -r.sin(), 0.0],
            [r.sin(),  r.cos(), 0.0],
            [0.0,      0.0,     1.0],
        ])
    }

    #[inline]
    pub fn aplicar(m: &Matriz3x3, v: Vector3D) -> Vector3D {
        m.mul_vector(v)
    }
}
