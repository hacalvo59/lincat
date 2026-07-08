#[derive(Debug, Clone)]
pub enum ModoArcos {
    ArcosG2G3,
    SegmentosLineales,
}

#[derive(Debug, Clone)]
pub struct SelectorArcos {
    pub modo: ModoArcos,
}

impl SelectorArcos {
    pub fn nuevo(modo: &str) -> Self {
        let modo_final = match modo {
            "arcos" => ModoArcos::ArcosG2G3,
            "segmentos" => ModoArcos::SegmentosLineales,
            _ => ModoArcos::ArcosG2G3,
        };

        Self { modo: modo_final }
    }

    pub fn usar_arcos(&self) -> bool {
        matches!(self.modo, ModoArcos::ArcosG2G3)
    }
}
