env_data = {
    "ENV": "development",
    "DB_HOST": "localhost",
    "DB_PORT": "5432",
    "API_KEY": "12345-ABCDE"
}

with open(".env", "w") as f:
    for key, value in env_data.items():
        f.write(f"{key}={value}\n")

print(".env file created successfully!")