import json

cloud = {
    "provider": "AWS",
    "instance": "t2.micro",
    "region": "ap-south-1"
}

print("Provisioning:", json.dumps(cloud, indent=2))