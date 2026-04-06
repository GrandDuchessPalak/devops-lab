import subprocess

log = subprocess.check_output("git log --oneline", shell=True)
print(log.decode())
