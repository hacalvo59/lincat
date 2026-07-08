use serde_json::json;
use crate::core::vector3d::Vector3D;

pub fn op_normalizar_vector(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let x = v["x"].as_f64().unwrap_or(0.0) as f32;
    let y = v["y"].as_f64().unwrap_or(0.0) as f32;
    let z = v["z"].as_f64().unwrap_or(0.0) as f32;

    let vec = Vector3D::new(x, y, z);
    let norm = vec.normalize();

    let out = json!({
        "vector_normalizado": {
            "x": norm.x,
            "y": norm.y,
            "z": norm.z
        },
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
