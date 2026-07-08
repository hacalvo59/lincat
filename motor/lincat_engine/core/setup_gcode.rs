#[derive(Debug, Clone)]
pub struct SetupGcode {
    pub modo_relativo: bool,   // G90 / G91
    pub usar_mm: bool,         // G21 / G20
    pub feedrate: f32,         // F
    pub plano: String,         // G17 / G18 / G19
    pub offset: String,        // G54 / G55 / G56
    pub usar_arcos: bool,      // G2/G3 o segmentos
}

impl SetupGcode {
    pub fn nuevo(
        modo: &str,
        unidad: &str,
        feedrate: f32,
        plano: &str,
        offset: &str,
        usar_arcos: bool
    ) -> Self {

        let modo_relativo = modo == "relativo";
        let usar_mm = unidad == "mm";

        Self {
            modo_relativo,
            usar_mm,
            feedrate,
            plano: plano.to_string(),
            offset: offset.to_string(),
            usar_arcos,
        }
    }
}
