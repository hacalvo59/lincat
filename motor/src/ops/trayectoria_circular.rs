use serde_json::json;
use crate::core::point3d::Point3D;
use crate::core::trayectoria_circular::TrayectoriaCircular;

pub fn op_trayectoria_circular(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let ini = v["inicio"].clone();
    let fin = v["fin"].clone();
    let cen = v["centro"].clone();

    let pasos = v["pasos"].as_u64().unwrap_or(20) as usize;
    let sentido = v["sentido"].as_str().unwrap_or("ccw") == "ccw";

    let inicio = Point3D::new(
        ini["x"].as_f64().unwrap_or(0.0) as f32,
        ini["y"].as_f64().unwrap_or(0.0) as f32,
        ini["z"].as_f64().unwrap_or(0.0) as f32,
    );

    let fin = Point3D::new(
        fin["x"].as_f64().unwrap_or(0.0) as f32,
        fin["y"].as_f64().unwrap_or(0.0) as f32,
        fin["z"].as_f64().unwrap_or(0.0) as f32,
    );

    let centro = Point3D::new(
        cen["x"].as_f64().unwrap_or(0.0) as f32,
        cen["y"].as_f64().unwrap_or(0.0) as f32,
        cen["z"].as_f64().unwrap_or(0.0) as f32,
    );

    let tray = TrayectoriaCircular::generar(inicio, fin, centro, pasos, sentido);

    let puntos_json: Vec<_> = tray.puntos.iter().map(|p| {
        json!({ "x": p.x, "y": p.y, "z": p.z })
    }).collect();

    let out = json!({
        "trayectoria_circular": puntos_json,
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
