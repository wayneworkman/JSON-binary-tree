#!/usr/bin/python
import json


object = {"+": [5, {"-":[9,8]}]}


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
print 'Solution: ' + str(eval(math))

