use serde_json::json;
use crate::core::recta3d::Recta3D;
use crate::core::point3d::Point3D;
use crate::core::vector3d::Vector3D;

pub fn op_recta3d(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let px = v["punto"]["x"].as_f64().unwrap_or(0.0) as f32;
    let py = v["punto"]["y"].as_f64().unwrap_or(0.0) as f32;
    let pz = v["punto"]["z"].as_f64().unwrap_or(0.0) as f32;

    let dx = v["direccion"]["x"].as_f64().unwrap_or(0.0) as f32;
    let dy = v["direccion"]["y"].as_f64().unwrap_or(0.0) as f32;
    let dz = v["direccion"]["z"].as_f64().unwrap_or(0.0) as f32;

    let recta = Recta3D::new(
        Point3D::new(px, py, pz),
        Vector3D::new(dx, dy, dz)
    );

    let out = json!({
        "recta3d": {
            "punto": { "x": recta.punto.x, "y": recta.punto.y, "z": recta.punto.z },
            "direccion": { "x": recta.direccion.x, "y": recta.direccion.y, "z": recta.direccion.z }
        },
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
