import subprocess

subprocess.run("git add .", shell=True)
subprocess.run("git commit -m 'update'", shell=True)
subprocess.run("docker build -t app .", shell=True)