use crate::core::matriz3x3::Matriz3x3;
use crate::core::vector3d::Vector3D;

pub struct Transformaciones3D;

impl Transformaciones3D {

    pub fn rotacion_x(grados: f32) -> Matriz3x3 {
        let r = grados.to_radians();
        Matriz3x3::new([
            [1.0, 0.0, 0.0],
            [0.0, r.cos(), -r.sin()],
            [0.0, r.sin(),  r.cos()],
        ])
    }

    pub fn rotacion_y(grados: f32) -> Matriz3x3 {
        let r = grados.to_radians();
        Matriz3x3::new([
            [ r.cos(), 0.0, r.sin()],
            [ 0.0,    1.0, 0.0   ],
            [-r.sin(), 0.0, r.cos()],
        ])
    }

    pub fn rotacion_z(grados: f32) -> Matriz3x3 {
        let r = grados.to_radians();
        Matriz3x3::new([
            [r.cos(), -r.sin(), 0.0],
            [r.sin(),  r.cos(), 0.0],
            [0.0,      0.0,     1.0],
        ])
    }

    pub fn aplicar(m: &Matriz3x3, v: Vector3D) -> Vector3D {
        m.mul_vector(v)
    }
}
use crate::core::matriz3x3::Matriz3x3;
use crate::core::vector3d::Vector3D;

pub struct Transformaciones3D;

impl Transformaciones3D {
    // ... rotacion_x / y / z que ya tenés ...

    pub fn rotacion_eje(grados: f32, eje: Vector3D) -> Matriz3x3 {
        let u = eje.normalize();
        let r = grados.to_radians();
        let c = r.cos();
        let s = r.sin();
        let ux = u.x;
        let uy = u.y;
        let uz = u.z;

        Matriz3x3::new([
            [
                c + ux*ux*(1.0 - c),
                ux*uy*(1.0 - c) - uz*s,
                ux*uz*(1.0 - c) + uy*s,
            ],
            [
                uy*ux*(1.0 - c) + uz*s,
                c + uy*uy*(1.0 - c),
                uy*uz*(1.0 - c) - ux*s,
            ],
            [
                uz*ux*(1.0 - c) - uy*s,
                uz*uy*(1.0 - c) + ux*s,
                c + uz*uz*(1.0 - c),
            ],
        ])
    }

    pub fn aplicar(m: &Matriz3x3, v: Vector3D) -> Vector3D {
        m.mul_vector(v)
    }
}
