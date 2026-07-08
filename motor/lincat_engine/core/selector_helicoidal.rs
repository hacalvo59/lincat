#[derive(Debug, Clone)]
pub enum ModoHelicoidal {
    HelicoidalG2G3,
    SegmentosLineales,
}

#[derive(Debug, Clone)]
pub struct SelectorHelicoidal {
    pub modo: ModoHelicoidal,
}

impl SelectorHelicoidal {
    pub fn nuevo(modo: &str) -> Self {
        let modo_final = match modo {
            "helicoidal" => ModoHelicoidal::HelicoidalG2G3,
            "segmentos" => ModoHelicoidal::SegmentosLineales,
            _ => ModoHelicoidal::HelicoidalG2G3,
        };

        Self { modo: modo_final }
    }

    pub fn usar_helicoidal(&self) -> bool {
        matches!(self.modo, ModoHelicoidal::HelicoidalG2G3)
    }
}
