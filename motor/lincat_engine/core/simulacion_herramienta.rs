use crate::core::point3d::Point3D;

#[derive(Debug)]
pub struct EstadoHerramienta {
    pub posicion: Point3D,
    pub velocidad: f32,
    pub tiempo: f32,
}

#[derive(Debug)]
pub struct SimulacionHerramienta {
    pub estados: Vec<EstadoHerramienta>,
}

impl SimulacionHerramienta {
    pub fn generar(
        trayectoria: &Vec<Point3D>,
        velocidades: &Vec<f32>,
        tiempos: &Vec<f32>
    ) -> Self {

        let mut estados = Vec::new();

        for i in 0..trayectoria.len() {
            estados.push(EstadoHerramienta {
                posicion: trayectoria[i],
                velocidad: velocidades[i],
                tiempo: tiempos[i],
            });
        }

        Self { estados }
    }
}
