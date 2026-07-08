use crate::core::recta3d::Recta3D;
use crate::core::point3d::Point3D;
use crate::core::vector3d::Vector3D;

pub struct InterseccionRectaRecta;

impl InterseccionRectaRecta {

    pub fn calcular(r1: &Recta3D, r2: &Recta3D) -> Option<Point3D> {
        let p1 = r1.punto;
        let d1 = r1.direccion;
        let p2 = r2.punto;
        let d2 = r2.direccion;

        let cruz = d1.cross(&d2);

        // Si el producto cruzado es casi cero → rectas paralelas o coincidentes
        if cruz.magnitude() < 1e-6 {
            return None;
        }

        // Vector entre puntos
        let p21 = Vector3D::new(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z);

        // Fórmula industrial para t usando triple producto
        let t = p21.cross(&d2).dot(&cruz) / cruz.dot(&cruz);

        Some(r1.punto_en_t(t))
    }
}
