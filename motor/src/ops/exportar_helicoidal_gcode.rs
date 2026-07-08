use serde_json::json;
use crate::core::point3d::Point3D;
use crate::core::exportar_helicoidal_gcode::ExportadorHelicoidalGcode;

pub fn op_exportar_helicoidal_gcode(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let feed = v["feedrate"].as_f64().unwrap_or(300.0) as f32;
    let usar_mm = v["usar_mm"].as_bool().unwrap_or(true);
    let sentido_ccw = v["sentido"].as_str().unwrap_or("ccw") == "ccw";

    let centro = v["centro"].clone();
    let centro_x = centro["x"].as_f64().unwrap_or(0.0) as f32;
    let centro_y = centro["y"].as_f64().unwrap_or(0.0) as f32;

    let arr = v["trayectoria"].as_array().unwrap_or(&vec![]);
    let mut puntos = Vec::new();

    for p in arr {
        puntos.push(Point3D::new(
            p["x"].as_f64().unwrap_or(0.0) as f32,
            p["y"].as_f64().unwrap_or(0.0) as f32,
            p["z"].as_f64().unwrap_or(0.0) as f32,
        ));
    }

    let gcode = ExportadorHelicoidalGcode::desde_trayectoria(
        &puntos,
        feed,
        usar_mm,
        sentido_ccw,
        centro_x,
        centro_y
    );

    let out = json!({
        "gcode_helicoidal": gcode,
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
