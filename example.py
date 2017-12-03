#!/usr/bin/python
import json



keys = {}
for i in range(,):
    chars.append(str(chr(i)))
keyLength = len(keys) - 1


digits = []
for i in range(40,57):
    digits.append(str(chr(i)))
digitLength = len(digits) - 1




# start at the top, treat every level the same.
# Decide randomly - is this a key or a digit?
# If it's a digit, it's tree ends there. If it's a key, it must produce underneath itself.
# we can change the probability of key vs digit by weighing keys more heavily, so we get larger equations.


object = {"+": [5, {"-":[9,'-']}]}


def iterate(object):
    if isinstance(object,dict):
        for key, item in object.items():
            leftItem = item[0]
            rightItem = item[1]
            if isinstance(leftItem,dict):
                return iterate(item)
            else:
                return str(leftItem) + str(key) + str( iterate(rightItem) )
    else:
        return object




print 'JSON problem: ' + json.dumps(object)
math = iterate(object)
print 'Problem: ' + math
try:
    print 'Solution: ' + str(eval(math))
except:
    print 'Invalid or malformed mathmatical problem'

