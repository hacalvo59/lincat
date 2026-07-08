use serde_json::json;
use crate::core::vector3d::Vector3D;

pub fn op_suma_vector(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let ax = v["a"]["x"].as_f64().unwrap_or(0.0) as f32;
    let ay = v["a"]["y"].as_f64().unwrap_or(0.0) as f32;
    let az = v["a"]["z"].as_f64().unwrap_or(0.0) as f32;

    let bx = v["b"]["x"].as_f64().unwrap_or(0.0) as f32;
    let by = v["b"]["y"].as_f64().unwrap_or(0.0) as f32;
    let bz = v["b"]["z"].as_f64().unwrap_or(0.0) as f32;

    let v1 = Vector3D::new(ax, ay, az);
    let v2 = Vector3D::new(bx, by, bz);

    let suma = v1.add(&v2);

    let out = json!({
        "suma_vector": {
            "x": suma.x,
            "y": suma.y,
            "z": suma.z
        },
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
