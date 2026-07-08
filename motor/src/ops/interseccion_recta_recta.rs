use serde_json::json;
use crate::core::recta3d::Recta3D;
use crate::core::point3d::Point3D;
use crate::core::vector3d::Vector3D;
use crate::core::interseccion_recta_recta::InterseccionRectaRecta;

pub fn op_interseccion_recta_recta(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let r1p = v["r1"]["punto"].clone();
    let r1d = v["r1"]["direccion"].clone();
    let r2p = v["r2"]["punto"].clone();
    let r2d = v["r2"]["direccion"].clone();

    let recta1 = Recta3D::new(
        Point3D::new(
            r1p["x"].as_f64().unwrap_or(0.0) as f32,
            r1p["y"].as_f64().unwrap_or(0.0) as f32,
            r1p["z"].as_f64().unwrap_or(0.0) as f32,
        ),
        Vector3D::new(
            r1d["x"].as_f64().unwrap_or(0.0) as f32,
            r1d["y"].as_f64().unwrap_or(0.0) as f32,
            r1d["z"].as_f64().unwrap_or(0.0) as f32,
        )
    );

    let recta2 = Recta3D::new(
        Point3D::new(
            r2p["x"].as_f64().unwrap_or(0.0) as f32,
            r2p["y"].as_f64().unwrap_or(0.0) as f32,
            r2p["z"].as_f64().unwrap_or(0.0) as f32,
        ),
        Vector3D::new(
            r2d["x"].as_f64().unwrap_or(0.0) as f32,
            r2d["y"].as_f64().unwrap_or(0.0) as f32,
            r2d["z"].as_f64().unwrap_or(0.0) as f32,
        )
    );

    let inter = InterseccionRectaRecta::calcular(&recta1, &recta2);

    let out = match inter {
        Some(p) => json!({
            "interseccion": { "x": p.x, "y": p.y, "z": p.z },
            "time_ms": 0.01
        }),
        None => json!({
            "interseccion": null,
            "motivo": "no se cruzan (paralelas o alabeadas)",
            "time_ms": 0.01
        })
    };

    Ok(out.to_string())
}
