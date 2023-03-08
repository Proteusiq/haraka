# Requirements



# Speed
```sh
apt install hyperfine

hyperfine --warmup 3 'python -m benchmark -s 10000000 -k pu' 'python -m benchmark -s 10000000 -k op' 'python -m benchmark -s 10000000 -k rs'
```

# Memory
```sh
pip install memray

memray run --live -m benchmark -s 10000000 -k py
```