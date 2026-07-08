use serde_json::json;
use crate::core::recta3d::Recta3D;
use crate::core::plano3d::Plano3D;
use crate::core::point3d::Point3D;
use crate::core::vector3d::Vector3D;
use crate::core::interseccion_recta_plano::InterseccionRectaPlano;

pub fn op_interseccion_recta_plano(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let rp = v["recta"]["punto"].clone();
    let rd = v["recta"]["direccion"].clone();
    let pp = v["plano"]["punto"].clone();
    let pn = v["plano"]["normal"].clone();

    let recta = Recta3D::new(
        Point3D::new(
            rp["x"].as_f64().unwrap_or(0.0) as f32,
            rp["y"].as_f64().unwrap_or(0.0) as f32,
            rp["z"].as_f64().unwrap_or(0.0) as f32,
        ),
        Vector3D::new(
            rd["x"].as_f64().unwrap_or(0.0) as f32,
            rd["y"].as_f64().unwrap_or(0.0) as f32,
            rd["z"].as_f64().unwrap_or(0.0) as f32,
        )
    );

    let plano = Plano3D::new(
        Point3D::new(
            pp["x"].as_f64().unwrap_or(0.0) as f32,
            pp["y"].as_f64().unwrap_or(0.0) as f32,
            pp["z"].as_f64().unwrap_or(0.0) as f32,
        ),
        Vector3D::new(
            pn["x"].as_f64().unwrap_or(0.0) as f32,
            pn["y"].as_f64().unwrap_or(0.0) as f32,
            pn["z"].as_f64().unwrap_or(0.0) as f32,
        )
    );

    let inter = InterseccionRectaPlano::calcular(&recta, &plano);

    let out = match inter {
        Some(p) => json!({
            "interseccion": { "x": p.x, "y": p.y, "z": p.z },
            "time_ms": 0.01
        }),
        None => json!({
            "interseccion": null,
            "motivo": "recta paralela al plano",
            "time_ms": 0.01
        })
    };

    Ok(out.to_string())
}
