#!/usr/bin/python
import fileinput


def stack_strings(strings):
    result = ''
    for i,s in enumerate(strings):
        if (i % 2) == 0:
            l = len(s)
            l_mutate = lambda x: x - 1
            l_isdone = lambda x: x<1
        else:
            l = 1
            l_mutate = lambda x: x + 1
            l_isdone = lambda x: x>=len(s)
        
        while not l_isdone(l):
                if s[l-1] != ' ':
                    result = result + s[0:l] + "\n"
                l = l_mutate(l)
    return result.rstrip()



if __name__ == '__main__':
    output = ''
    lines = [line for line in fileinput.input()]

    for line in lines:
        strings = line.split(':')
        output = output + stack_strings(strings)

    print output
