use std::collections::HashMap;
use rand::{Rng, rngs::ThreadRng};

pub fn dice_simulate(s:i64) -> HashMap<i8, f64> {
    let mut storage: HashMap<i8, f64> = HashMap::new();
    let mut rng: ThreadRng = rand::thread_rng();

    for _ in 0..s {
        let num: i8  = rng.gen_range(1..7);
        let prob: &mut f64 =  storage.entry(num).or_insert(0.);
        *prob += 1./ s as f64;
    }

    storage
}

