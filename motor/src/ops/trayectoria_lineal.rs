use serde_json::json;
use crate::core::point3d::Point3D;
use crate::core::trayectoria_lineal::TrayectoriaLineal;

pub fn op_trayectoria_lineal(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let p1 = v["inicio"].clone();
    let p2 = v["fin"].clone();
    let pasos = v["pasos"].as_u64().unwrap_or(10) as usize;

    let inicio = Point3D::new(
        p1["x"].as_f64().unwrap_or(0.0) as f32,
        p1["y"].as_f64().unwrap_or(0.0) as f32,
        p1["z"].as_f64().unwrap_or(0.0) as f32,
    );

    let fin = Point3D::new(
        p2["x"].as_f64().unwrap_or(0.0) as f32,
        p2["y"].as_f64().unwrap_or(0.0) as f32,
        p2["z"].as_f64().unwrap_or(0.0) as f32,
    );

    let tray = TrayectoriaLineal::generar(inicio, fin, pasos);

    let puntos_json: Vec<_> = tray.puntos.iter().map(|p| {
        json!({ "x": p.x, "y": p.y, "z": p.z })
    }).collect();

    let out = json!({
        "trayectoria_lineal": puntos_json,
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
