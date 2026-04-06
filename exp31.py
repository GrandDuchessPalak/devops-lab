import subprocess

subprocess.run("git pull", shell=True)
subprocess.run("pytest", shell=True)
subprocess.run("docker build -t app .", shell=True)
subprocess.run("docker run app", shell=True)