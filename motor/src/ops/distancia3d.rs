use serde_json::json;
use crate::core::point3d::Point3D;

pub fn op_distancia3d(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let ax = v["a"]["x"].as_f64().unwrap_or(0.0) as f32;
    let ay = v["a"]["y"].as_f64().unwrap_or(0.0) as f32;
    let az = v["a"]["z"].as_f64().unwrap_or(0.0) as f32;

    let bx = v["b"]["x"].as_f64().unwrap_or(0.0) as f32;
    let by = v["b"]["y"].as_f64().unwrap_or(0.0) as f32;
    let bz = v["b"]["z"].as_f64().unwrap_or(0.0) as f32;

    let p1 = Point3D::new(ax, ay, az);
    let p2 = Point3D::new(bx, by, bz);

    let dist = p1.distance(&p2);

    let out = json!({
        "distancia": dist,
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
