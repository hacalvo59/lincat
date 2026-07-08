use serde_json::json;
use crate::core::plano3d::Plano3D;
use crate::core::point3d::Point3D;
use crate::core::vector3d::Vector3D;

pub fn op_plano3d(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let px = v["punto"]["x"].as_f64().unwrap_or(0.0) as f32;
    let py = v["punto"]["y"].as_f64().unwrap_or(0.0) as f32;
    let pz = v["punto"]["z"].as_f64().unwrap_or(0.0) as f32;

    let nx = v["normal"]["x"].as_f64().unwrap_or(0.0) as f32;
    let ny = v["normal"]["y"].as_f64().unwrap_or(0.0) as f32;
    let nz = v["normal"]["z"].as_f64().unwrap_or(0.0) as f32;

    let plano = Plano3D::new(
        Point3D::new(px, py, pz),
        Vector3D::new(nx, ny, nz)
    );

    let out = json!({
        "plano3d": {
            "punto": { "x": plano.punto.x, "y": plano.punto.y, "z": plano.punto.z },
            "normal": { "x": plano.normal.x, "y": plano.normal.y, "z": plano.normal.z }
        },
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
