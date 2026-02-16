import subprocess

subprocess.run(['git', 'branch', 'feature1'])
subprocess.run(['git', 'checkout', 'feature1'])

with open('demo.txt', 'w') as f:
    f.write('Feature branch work')

subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Feature commit'])

subprocess.run(['git', 'checkout', 'main'])
subprocess.run(['git', 'merge', 'feature1'])

print('Branching and merging completed')
