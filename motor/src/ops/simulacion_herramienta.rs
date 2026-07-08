use serde_json::json;
use crate::core::point3d::Point3D;
use crate::core::simulacion_herramienta::SimulacionHerramienta;

pub fn op_simulacion_herramienta(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let puntos_json = v["trayectoria"].as_array().unwrap_or(&vec![]);
    let velocidades_json = v["velocidades"].as_array().unwrap_or(&vec![]);
    let tiempos_json = v["tiempos"].as_array().unwrap_or(&vec![]);

    let mut trayectoria = Vec::new();
    let mut velocidades = Vec::new();
    let mut tiempos = Vec::new();

    for p in puntos_json {
        trayectoria.push(Point3D::new(
            p["x"].as_f64().unwrap_or(0.0) as f32,
            p["y"].as_f64().unwrap_or(0.0) as f32,
            p["z"].as_f64().unwrap_or(0.0) as f32,
        ));
    }

    for v in velocidades_json {
        velocidades.push(v.as_f64().unwrap_or(0.0) as f32);
    }

    for t in tiempos_json {
        tiempos.push(t.as_f64().unwrap_or(0.0) as f32);
    }

    let sim = SimulacionHerramienta::generar(&trayectoria, &velocidades, &tiempos);

    let salida: Vec<_> = sim.estados.iter().map(|e| {
        json!({
            "posicion": { "x": e.posicion.x, "y": e.posicion.y, "z": e.posicion.z },
            "velocidad": e.velocidad,
            "tiempo": e.tiempo
        })
    }).collect();

    let out = json!({
        "simulacion_herramienta": salida,
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
