import subprocess

log = subprocess.check_output("git log --oneline", shell=True).decode()

with open("report.txt", "w") as f:
    f.write("Git History:\n")
    f.write(log)

print("Report generated!")