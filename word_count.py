import argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

with open(args.filename, 'r') as f:
    print(Counter(f.read().split()))
