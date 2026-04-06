import argparse
import psutil

parser = argparse.ArgumentParser()
parser.add_argument("--cpu", action="store_true")
parser.add_argument("--memory", action="store_true")

args = parser.parse_args()

if args.cpu:
    print("CPU:", psutil.cpu_percent())

if args.memory:
    print("Memory:", psutil.virtual_memory().percent)