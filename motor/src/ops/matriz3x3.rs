use serde_json::json;
use crate::core::matriz3x3::Matriz3x3;
use crate::core::vector3d::Vector3D;

pub fn op_matriz3x3(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let mut m = [[0.0f32; 3]; 3];
    for i in 0..3 {
        for j in 0..3 {
            m[i][j] = v["m"][i][j].as_f64().unwrap_or(0.0) as f32;
        }
    }

    let vx = v["vector"]["x"].as_f64().unwrap_or(0.0) as f32;
    let vy = v["vector"]["y"].as_f64().unwrap_or(0.0) as f32;
    let vz = v["vector"]["z"].as_f64().unwrap_or(0.0) as f32;

    let mat = Matriz3x3::new(m);
    let vec = Vector3D::new(vx, vy, vz);
    let res = mat.mul_vector(vec);

    let out = json!({
        "resultado": { "x": res.x, "y": res.y, "z": res.z },
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
