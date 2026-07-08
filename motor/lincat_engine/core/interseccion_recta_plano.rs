use crate::core::recta3d::Recta3D;
use crate::core::plano3d::Plano3D;
use crate::core::point3d::Point3D;
use crate::core::vector3d::Vector3D;

pub struct InterseccionRectaPlano;

impl InterseccionRectaPlano {
    pub fn calcular(recta: &Recta3D, plano: &Plano3D) -> Option<Point3D> {
        let p0 = recta.punto;
        let d = recta.direccion;
        let pp = plano.punto;
        let n = plano.normal;

        let denom = d.dot(&n);
        if denom.abs() < 1e-6 {
            return None; // Recta paralela al plano
        }

        let t = Vector3D::new(pp.x - p0.x, pp.y - p0.y, pp.z - p0.z).dot(&n) / denom;

        Some(recta.punto_en_t(t))
    }
}
