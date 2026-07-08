use serde_json::json;
use crate::core::vector3d::Vector3D;

pub fn op_angulo_vectores(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let ax = v["a"]["x"].as_f64().unwrap_or(0.0) as f32;
    let ay = v["a"]["y"].as_f64().unwrap_or(0.0) as f32;
    let az = v["a"]["z"].as_f64().unwrap_or(0.0) as f32;

    let bx = v["b"]["x"].as_f64().unwrap_or(0.0) as f32;
    let by = v["b"]["y"].as_f64().unwrap_or(0.0) as f32;
    let bz = v["b"]["z"].as_f64().unwrap_or(0.0) as f32;

    let a = Vector3D::new(ax, ay, az);
    let b = Vector3D::new(bx, by, bz);

    let dot = a.dot(&b);
    let mag_a = a.magnitude();
    let mag_b = b.magnitude();

    if mag_a == 0.0 || mag_b == 0.0 {
        return Ok(json!({
            "angulo_rad": 0.0,
            "angulo_deg": 0.0,
            "time_ms": 0.01
        }).to_string());
    }

    let cos_theta = (dot / (mag_a * mag_b)).clamp(-1.0, 1.0);
    let angulo_rad = cos_theta.acos();
    let angulo_deg = angulo_rad.to_degrees();

    let out = json!({
        "angulo_rad": angulo_rad,
        "angulo_deg": angulo_deg,
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
