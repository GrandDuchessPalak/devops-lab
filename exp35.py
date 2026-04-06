import re

with open("app.py") as f:
    data = f.read()

if re.search(r'password\s*=', data):
    print("⚠️ Hardcoded password found!")