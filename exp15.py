import subprocess

log = subprocess.check_output(['git', 'log', '--oneline']).decode()

commits = log.splitlines()
print('Total Commits:', len(commits))

with open('git_report.txt', 'w') as f:
    f.write('Git Commit Report\n')
    f.write('Total Commits: ' + str(len(commits)))

