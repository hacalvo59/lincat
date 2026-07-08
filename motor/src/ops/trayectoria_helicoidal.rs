use serde_json::json;
use crate::core::point3d::Point3D;
use crate::core::trayectoria_helicoidal::TrayectoriaHelicoidal;

pub fn op_trayectoria_helicoidal(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let cen = v["centro"].clone();
    let centro = Point3D::new(
        cen["x"].as_f64().unwrap_or(0.0) as f32,
        cen["y"].as_f64().unwrap_or(0.0) as f32,
        cen["z"].as_f64().unwrap_or(0.0) as f32,
    );

    let radio = v["radio"].as_f64().unwrap_or(1.0) as f32;
    let z_inicio = v["z_inicio"].as_f64().unwrap_or(0.0) as f32;
    let z_fin = v["z_fin"].as_f64().unwrap_or(0.0) as f32;
    let vueltas = v["vueltas"].as_f64().unwrap_or(1.0) as f32;
    let pasos = v["pasos"].as_u64().unwrap_or(50) as usize;
    let sentido = v["sentido"].as_str().unwrap_or("ccw") == "ccw";

    let tray = TrayectoriaHelicoidal::generar(
        centro, radio, z_inicio, z_fin, vueltas, pasos, sentido
    );

    let puntos_json: Vec<_> = tray.puntos.iter().map(|p| {
        json!({ "x": p.x, "y": p.y, "z": p.z })
    }).collect();

    let out = json!({
        "trayectoria_helicoidal": puntos_json,
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
