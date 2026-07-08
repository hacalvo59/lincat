use serde_json::json;
use crate::core::point3d::Point3D;
use crate::core::trayectoria_spline::TrayectoriaSpline;

pub fn op_trayectoria_spline(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let pasos = v["pasos"].as_u64().unwrap_or(20) as usize;

    let arr = v["puntos_control"].as_array().unwrap_or(&vec![]);
    let mut puntos_control = Vec::new();

    for p in arr {
        puntos_control.push(Point3D::new(
            p["x"].as_f64().unwrap_or(0.0) as f32,
            p["y"].as_f64().unwrap_or(0.0) as f32,
            p["z"].as_f64().unwrap_or(0.0) as f32,
        ));
    }

    let tray = TrayectoriaSpline::generar(&puntos_control, pasos);

    let salida: Vec<_> = tray.puntos.iter().map(|p| {
        json!({ "x": p.x, "y": p.y, "z": p.z })
    }).collect();

    let out = json!({
        "trayectoria_spline": salida,
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
