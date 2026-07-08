use serde_json::json;
use crate::core::selector_arcos::SelectorArcos;

pub fn selector_arcos(input_json: &str) -> Result<String, String> {
    let v: serde_json::Value = serde_json::from_str(input_json)
        .map_err(|e| format!("JSON error: {e}"))?;

    let modo = v["modo"].as_str().unwrap_or("arcos");

    let selector = SelectorArcos::nuevo(modo);

    let out = json!({
        "selector_arcos": {
            "usar_arcos": selector.usar_arcos(),
            "modo": modo
        },
        "time_ms": 0.01
    });

    Ok(out.to_string())
}
