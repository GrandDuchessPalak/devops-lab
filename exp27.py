import subprocess

result = subprocess.run("docker ps", shell=True, capture_output=True, text=True)
print(result.stdout)