use serde_json::json;
use crate::core::point3d::Point3D;
use crate::core::interpolacion_velocidad::InterpolacionVelocidad;

pub fn op_interpolacion_velocidad(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let v_max = v["v_max"].as_f64().unwrap_or(100.0) as f32;
    let a_max = v["a_max"].as_f64().unwrap_or(200.0) as f32;

    let arr = v["trayectoria"].as_array().unwrap_or(&vec![]);
    let mut trayectoria = Vec::new();

    for p in arr {
        trayectoria.push(Point3D::new(
            p["x"].as_f64().unwrap_or(0.0) as f32,
            p["y"].as_f64().unwrap_or(0.0) as f32,
            p["z"].as_f64().unwrap_or(0.0) as f32,
        ));
    }

    let interp = InterpolacionVelocidad::generar(&trayectoria, v_max, a_max);

    let salida: Vec<_> = interp.puntos.iter().map(|pv| {
        json!({
            "punto": { "x": pv.punto.x, "y": pv.punto.y, "z": pv.punto.z },
            "velocidad": pv.velocidad,
            "tiempo": pv.tiempo
        })
    }).collect();

    let out = json!({
        "interpolacion_velocidad": salida,
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
