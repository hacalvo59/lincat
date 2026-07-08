use serde_json::json;
use crate::core::vector3d::Vector3D;

pub fn op_proyeccion_vector(input_json: &str) -> Result<String, String> {
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

    let dot_ab = a.dot(&b);
    let dot_bb = b.dot(&b);

    if dot_bb == 0.0 {
        return Ok(json!({
            "proyeccion": { "x": 0.0, "y": 0.0, "z": 0.0 },
            "time_ms": 0.01
        }).to_string());
    }

    let escala = dot_ab / dot_bb;
    let proy = Vector3D::new(b.x * escala, b.y * escala, b.z * escala);

    let out = json!({
        "proyeccion": {
            "x": proy.x,
            "y": proy.y,
            "z": proy.z
        },
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
