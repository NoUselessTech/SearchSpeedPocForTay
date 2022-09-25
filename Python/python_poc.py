#!/usr/bin/python3
import re
import time
from sys import argv


print("Doing the long regex method")

print("Regex: /.*dolor.*elit.*do.*/")

long_regex = re.compile(".*dolor.*elit.*do.*")

# Open the source text
start_time = time.time()
with open('../lookup.txt') as source_file:
    for line in source_file.readlines():
        re.match(long_regex, line)
end_time = time.time()

print("Run time with long regex", int((end_time-start_time)*10000))

print("\r\nDoing the individual, parallel lookup method")

# Open the source text
start_time = time.time()
with open('../lookup.txt') as source_file:
    for line in source_file.readlines():
        line.find("dolor") and line.find("elit") and line.find("do") 
end_time = time.time()
print("Run time with individual parallel lookup method", int((end_time-start_time)*10000))

print("\r\nDoing the individual, serial lookup method")

# Open the source text
start_time = time.time()
with open('../lookup.txt') as source_file:
    for line in source_file.readlines():
        if line.find("dolor"):
            if line.find("elit"):
                line.find("do") 
end_time = time.time()
print("Run time with individual serial lookup method", int((end_time-start_time)*10000))
