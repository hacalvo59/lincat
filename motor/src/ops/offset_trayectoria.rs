use serde_json::json;
use crate::core::point3d::Point3D;
use crate::core::vector3d::Vector3D;
use crate::core::offset_trayectoria::OffsetTrayectoria;

pub fn op_offset_trayectoria(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let offset = v["offset"].as_f64().unwrap_or(0.0) as f32;

    let normal = Vector3D::new(
        v["normal"]["x"].as_f64().unwrap_or(0.0) as f32,
        v["normal"]["y"].as_f64().unwrap_or(0.0) as f32,
        v["normal"]["z"].as_f64().unwrap_or(0.0) as f32,
    );

    let puntos_json = v["trayectoria"].as_array().unwrap_or(&vec![]);

    let mut puntos = Vec::new();
    for p in puntos_json {
        puntos.push(Point3D::new(
            p["x"].as_f64().unwrap_or(0.0) as f32,
            p["y"].as_f64().unwrap_or(0.0) as f32,
            p["z"].as_f64().unwrap_or(0.0) as f32,
        ));
    }

    let tray_offset = OffsetTrayectoria::generar(&puntos, offset, normal);

    let salida: Vec<_> = tray_offset.puntos.iter().map(|p| {
        json!({ "x": p.x, "y": p.y, "z": p.z })
    }).collect();

    let out = json!({
        "trayectoria_offset": salida,
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
