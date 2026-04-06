import subprocess

print("Deploying application...")

# Example: pulling latest code
subprocess.run("git pull", shell=True)

# Example: restarting app (simulate)
print("Restarting application...")

print("Deployment successful ✅")