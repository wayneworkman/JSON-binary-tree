#!/usr/bin/python
import json
import random
import decimal

keys = []
for i in ('+','-','*','/'):
    keys.append(i)

digits = []
for i in range(40,57):
    digits.append(str(chr(i)))

def randomDecimal():
    return round(random.uniform(-10,10),4)

def assignKey():
    my_list = [True] * 50 + [False] * 50
    return random.choice(my_list)

def fillSpot():
    if assignKey():
        tmp = {}
        key = random.choice(keys)
        tmp[key] = []
        tmp[key].append(fillSpot())
        tmp[key].append(fillSpot())
        return tmp
    else:
        return randomDecimal()

def iterate(object):
    if isinstance(object,dict):
        for key, item in object.items():
            leftItem = item[0]
            rightItem = item[1]
            return str( iterate(leftItem) ) + str(key) + str( iterate(rightItem) )
    else:
        return str(object)


object = fillSpot()
print 'JSON problem: ' + json.dumps(object)
math = iterate(object)
print 'Problem: ' + str(math)
try:
    print 'Solution: ' + str(eval(math))
except:
    print 'Invalid or malformed mathmatical problem'




