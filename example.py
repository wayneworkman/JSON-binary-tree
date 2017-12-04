#!/usr/bin/python
import json
import random
import decimal

keys = []
for i in ('+','-','*','/'):
    keys.append(i)
keyLength = len(keys) - 1

digits = []
for i in range(40,57):
    digits.append(str(chr(i)))
digitLength = len(digits) - 1

def randomDecimal():
    return decimal.Decimal(str(random.random()))

def assignKey():
    my_list = [True] * 90 + [False] * 10
    return random.choice(my_list)

def fillSpot():
    if assignKey:
        key = random.choice(keys)
        object[key] = fillSpot
        return object
    else:
        return randomDecimal

def iterate(object):
    if isinstance(object,dict):
        for key, item in object.items():
            leftItem = item[0]
            rightItem = item[1]
            return str( iterate(leftItem) ) + str(key) + str( iterate(rightItem) )
    else:
        return str(object)

object = fillSpot

math = iterate(object)
print 'Problem: ' + str(math)
try:
    print 'Solution: ' + str(eval(math))
except:
    print 'Invalid or malformed mathmatical problem'

