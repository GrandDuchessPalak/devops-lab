import subprocess
subprocess.run(["git", "init"])
# Create a file
with open("test.txt", "w") as f:
    f.write("Hello DevOps")

# Add and commit
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial commit"])
