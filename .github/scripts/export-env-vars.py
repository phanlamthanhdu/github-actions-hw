import os

env_vars = os.getenv("env_vars").strip().split("\n")

print(env_vars)

for var in env_vars:
    print(f"::add-mask::{var.split("=")[1]}")