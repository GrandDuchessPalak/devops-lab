import subprocess

print("Running tests...")

result = subprocess.run("pytest", shell=True)

if result.returncode == 0:
    print("All tests passed ✅")
else:
    print("Tests failed ❌")