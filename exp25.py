import json

infra = {
    "vm_name": "dev-server",
    "cpu": "2 cores",
    "ram": "4GB",
    "disk": "50GB"
}

with open("infra.json", "w") as f:
    json.dump(infra, f, indent=4)

print("Infrastructure config created!")
