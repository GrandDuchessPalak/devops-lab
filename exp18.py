import os, time

path = "."

before = dict([(f, None) for f in os.listdir(path)])

while True:
    time.sleep(5)
    after = dict([(f, None) for f in os.listdir(path)])
    added = [f for f in after if not f in before]
    
    if added:
        print("Added:", added)
    
    before = after