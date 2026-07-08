use serde_json::json;
use crate::core::transformaciones3d::Transformaciones3D;
use crate::core::vector3d::Vector3D;

pub fn op_rotacion_vector(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let grados = v["grados"].as_f64().unwrap_or(0.0) as f32;

    let ax = v["eje"]["x"].as_f64().unwrap_or(0.0) as f32;
    let ay = v["eje"]["y"].as_f64().unwrap_or(0.0) as f32;
    let az = v["eje"]["z"].as_f64().unwrap_or(0.0) as f32;

    let vx = v["vector"]["x"].as_f64().unwrap_or(0.0) as f32;
    let vy = v["vector"]["y"].as_f64().unwrap_or(0.0) as f32;
    let vz = v["vector"]["z"].as_f64().unwrap_or(0.0) as f32;

    let eje = Vector3D::new(ax, ay, az);
    let vec = Vector3D::new(vx, vy, vz);

    let matriz = Transformaciones3D::rotacion_eje(grados, eje);
    let res = Transformaciones3D::aplicar(&matriz, vec);

    let out = json!({
        "resultado": { "x": res.x, "y": res.y, "z": res.z },
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
