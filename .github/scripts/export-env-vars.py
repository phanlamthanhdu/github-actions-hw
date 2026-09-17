import os


print(os.environ)

# env_vars = os.getenv("env_vars", "").strip().splitlines()

# print(env_vars)

# for var in env_vars:
#     key, value = var.split("=", 1)

#     os.environ[key] = value

#     print(f"::add-mask::{value}")