use serde_json::json;
use crate::core::selector_helicoidal::SelectorHelicoidal;

pub fn selector_helicoidal(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let modo = v["modo"].as_str().unwrap_or("helicoidal");

    let selector = SelectorHelicoidal::nuevo(modo);

    let out = json!({
        "selector_helicoidal": {
            "usar_helicoidal": selector.usar_helicoidal(),
            "modo": modo
        },
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
