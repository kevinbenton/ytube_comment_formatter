#!/usr/bin/python
import fileinput

output = ''
lines = [line for line in fileinput.input()]

for line in lines:
    strings = line.split(':')
    for i,s in enumerate(strings):
        if (i % 2) == 0:
            l = len(s)
            while l>0:
                output = output + s[0:l] + "\n"
                l = l - 1
        else:
            l = 1
            while l<len(s):
                output = output + s[0:l] + "\n"
                l = l + 1

print output
