import subprocess

container = input("Enter container name: ")
subprocess.run(f"docker logs {container}", shell=True)