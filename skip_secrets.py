import sys
import os

if len(sys.argv) != 2:
    exit(1)

filename = sys.argv[1]

if not os.access(filename, os.R_OK):
    exit(1)

file = open(filename, "r")
res = open("out.txt", "w")
while True:
    line = file.readline()
    if not line:
        break
    if "pineapple" not in line:
        res.write(line)

res.close()
file.close()