import shutil

try:
    shutil.copy("app.py", "backup.py")
    raise Exception("Deployment failed")
except:
    shutil.copy("backup.py", "app.py")
    print("Rollback successful!")