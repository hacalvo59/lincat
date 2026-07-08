use crate::core::point3d::Point3D;

#[derive(Debug)]
pub struct TrayectoriaSpline {
    pub puntos: Vec<Point3D>,
}

impl TrayectoriaSpline {

    fn catmull_rom(p0: Point3D, p1: Point3D, p2: Point3D, p3: Point3D, t: f32) -> Point3D {
        let t2 = t * t;
        let t3 = t2 * t;

        let x =
            0.5 * (2.0*p1.x +
                (-p0.x + p2.x) * t +
                (2.0*p0.x - 5.0*p1.x + 4.0*p2.x - p3.x) * t2 +
                (-p0.x + 3.0*p1.x - 3.0*p2.x + p3.x) * t3);

        let y =
            0.5 * (2.0*p1.y +
                (-p0.y + p2.y) * t +
                (2.0*p0.y - 5.0*p1.y + 4.0*p2.y - p3.y) * t2 +
                (-p0.y + 3.0*p1.y - 3.0*p2.y + p3.y) * t3);

        let z =
            0.5 * (2.0*p1.z +
                (-p0.z + p2.z) * t +
                (2.0*p0.z - 5.0*p1.z + 4.0*p2.z - p3.z) * t2 +
                (-p0.z + 3.0*p1.z - 3.0*p2.z + p3.z) * t3);

        Point3D::new(x, y, z)
    }

    pub fn generar(puntos_control: &Vec<Point3D>, pasos: usize) -> Self {
        let mut salida = Vec::new();

        if puntos_control.len() < 4 {
            return Self { puntos: salida };
        }

        for i in 0..puntos_control.len() - 3 {
            let p0 = puntos_control[i];
            let p1 = puntos_control[i+1];
            let p2 = puntos_control[i+2];
            let p3 = puntos_control[i+3];

            for s in 0..=pasos {
                let t = s as f32 / pasos as f32;
                salida.push(Self::catmull_rom(p0, p1, p2, p3, t));
            }
        }

        Self { puntos: salida }
    }
}
