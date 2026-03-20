import subprocess

subprocess.run(['docker', 'build', '-t', 'python-app', '.'])
print('Docker image built successfully')
