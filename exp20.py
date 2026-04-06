import os

folders = ["src","tests","docs"]
for f in folders:
    if not os.path.exists(f):
        print(f, "Missing")
    else:
        print(f, "Exists")
