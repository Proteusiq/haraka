# Haraka

_haraka_ is a Swahili word for `swiftly`. The repository object is to show the advantage of supercharging Python 🐍 computation with Rust 🦀.

# Up & Running
```sh
apt install hyperfine

hyperfine --warmup 3 'python -m benchmark -s 10000000 -k pu' 'python -m benchmark -s 10000000 -k op' 'python -m benchmark -s 10000000 -k rs'
```

# Memory
```sh
pip install memray

memray run --live -m benchmark -s 10000000 -k py
```
