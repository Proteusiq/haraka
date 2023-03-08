use std::collections::HashMap;
use pyo3::prelude::*;


mod simulator;
use simulator::dice_simulate;

/// Simulate 6 sided-die 
#[pyfunction]
#[pyo3(name = "dice_simulate")]
fn sim(s:i64) -> PyResult<HashMap<i8, f64>> {
    Ok(dice_simulate(s))
}

/// A Python module implemented in Rust.
#[pymodule]
fn haraka(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sim, m)?)?;
    Ok(())
}