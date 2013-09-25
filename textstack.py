#!/usr/bin/python

strings = ['North Korea', "Doesn't even lift"]
output = ''
for i,s in enumerate(strings):
    if (i % 2) == 0:
        l = len(s)
        while l>0:
            output = output + s[0:l] + "\n"
            l = l - 1
    else:
        l = 1
        while l<=len(s):
            output = output + s[0:l] + "\n"
            l = l + 1

print output
