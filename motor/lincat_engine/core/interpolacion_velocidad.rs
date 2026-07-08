use crate::core::point3d::Point3D;

#[derive(Debug)]
pub struct PuntoVelocidad {
    pub punto: Point3D,
    pub velocidad: f32,
    pub tiempo: f32,
}

#[derive(Debug)]
pub struct InterpolacionVelocidad {
    pub puntos: Vec<PuntoVelocidad>,
}

impl InterpolacionVelocidad {

    pub fn generar(
        trayectoria: &Vec<Point3D>,
        v_max: f32,
        a_max: f32
    ) -> Self {

        let mut salida = Vec::new();
        let mut tiempo_acumulado = 0.0;

        for i in 0..trayectoria.len() {
            let p = trayectoria[i];

            if i == 0 {
                salida.push(PuntoVelocidad {
                    punto: p,
                    velocidad: 0.0,
                    tiempo: 0.0,
                });
                continue;
            }

            let p_prev = trayectoria[i - 1];

            let dx = p.x - p_prev.x;
            let dy = p.y - p_prev.y;
            let dz = p.z - p_prev.z;

            let distancia = (dx*dx + dy*dy + dz*dz).sqrt();

            // Perfil trapezoidal simplificado
            let t_acel = v_max / a_max;
            let d_acel = 0.5 * a_max * t_acel * t_acel;

            let (velocidad, tiempo) = if distancia < 2.0 * d_acel {
                // No llega a velocidad máxima
                let t = (2.0 * distancia / a_max).sqrt();
                (a_max * t / 2.0, t)
            } else {
                // Perfil trapezoidal completo
                let d_const = distancia - 2.0 * d_acel;
                let t_const = d_const / v_max;
                let t_total = 2.0 * t_acel + t_const;
                (v_max, t_total)
            };

            tiempo_acumulado += tiempo;

            salida.push(PuntoVelocidad {
                punto: p,
                velocidad,
                tiempo: tiempo_acumulado,
            });
        }

        Self { puntos: salida }
    }
}
