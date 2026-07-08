pub fn op_generador_gcode(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let feed = v["feedrate"].as_f64().unwrap_or(300.0) as f32;
    let usar_mm = v["usar_mm"].as_bool().unwrap_or(true);
    let modo_relativo = v["modo"].as_str().unwrap_or("absoluto") == "relativo";

    let arr = v["trayectoria"].as_array().unwrap_or(&vec![]);
    let mut puntos = Vec::new();

    for p in arr {
        puntos.push(Point3D::new(
            p["x"].as_f64().unwrap_or(0.0) as f32,
            p["y"].as_f64().unwrap_or(0.0) as f32,
            p["z"].as_f64().unwrap_or(0.0) as f32,
        ));
    }

    let gcode = GeneradorGcode::desde_trayectoria(&puntos, feed, usar_mm, modo_relativo);

    let out = json!({
        "gcode": gcode,
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
