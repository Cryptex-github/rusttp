#[macro_use]
extern crate pyo3_built;
extern crate pyo3;


use pyo3::{prelude::*, wrap_pyfunction};

use reqwest;

#[allow(dead_code)]
mod build {
    include!(concat!(env!("OUT_DIR"), "/built.rs"));
}

/// Module documentation string
#[modinit("rusttp")]
fn init(py: Python, m: &PyModule) -> PyResult<()> {
    // ... //
    m.add("__build__", pyo3_built!(py, build))?;
    Ok(())
}


#[pyfunction]
fn get(py: Python, url: &str) -> PyResult<String> {
    pyo3_asyncio::tokio::future_into_py(py, async {
        Ok(reqwest::get(url).await?.text().await?)
    })
}

#[pymodule]
fn rusttp(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get, m)?)?;
    Ok(())
}
