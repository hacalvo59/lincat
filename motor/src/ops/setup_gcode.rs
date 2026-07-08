use serde_json::json;
use crate::core::setup_gcode::SetupGcode;

pub fn op_setup_gcode(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let modo = v["modo"].as_str().unwrap_or("absoluto");
    let unidad = v["unidad"].as_str().unwrap_or("mm");
    let feedrate = v["feedrate"].as_f64().unwrap_or(300.0) as f32;
    let plano = v["plano"].as_str().unwrap_or("G17");
    let offset = v["offset"].as_str().unwrap_or("G54");
    let usar_arcos = v["usar_arcos"].as_bool().unwrap_or(true);

    let setup = SetupGcode::nuevo(
        modo,
        unidad,
        feedrate,
        plano,
        offset,
        usar_arcos
    );

    let out = json!({
        "setup_gcode": {
            "modo_relativo": setup.modo_relativo,
            "usar_mm": setup.usar_mm,
            "feedrate": setup.feedrate,
            "plano": setup.plano,
            "offset": setup.offset,
            "usar_arcos": setup.usar_arcos
        },
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
