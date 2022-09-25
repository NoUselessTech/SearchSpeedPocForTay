#!/usr/bin/python3
import re
import time
from sys import argv


print("Doing the long regex method")

print("Regex: /.*dolor.*elit.*do.*/")

long_regex = re.compile(".*dolor.*elit.*do.*")
short_regex = [re.compile("dolor"), re.compile("elit"), re.compile("do")]

# Open the source text
start_time = time.time()
with open('../lookup.txt') as source_file:
    for line in source_file.readlines():
        re.match(long_regex, line)
end_time = time.time()

print("Run time with long regex", int((end_time-start_time)*10000))

print("\r\nDoing the individual, parallel lookup method with regex")

# Open the source text
start_time = time.time()
with open('../lookup.txt') as source_file:
    for line in source_file.readlines():
        re.match(short_regex[0], line) and re.match(short_regex[1], line) and re.match(short_regex[2], line) 
end_time = time.time()
print("Run time with individual parallel lookup method with regex", int((end_time-start_time)*10000))

print("\r\nDoing the individual, parallel lookup method")

print("\r\nDoing the individual, serial lookup method with regex")

# Open the source text
start_time = time.time()
with open('../lookup.txt') as source_file:
    for line in source_file.readlines():
        if re.match(short_regex[0], line):
            if re.match(short_regex[1], line):
                re.match(short_regex[2], line) 
end_time = time.time()
print("Run time with individual serial lookup method with regex", int((end_time-start_time)*10000))

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
