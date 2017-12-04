#!/usr/bin/python
import json
import random
import decimal
import sys

# Set recursion depth limit really high.
sys.setrecursionlimit(10000000)

decimalMinimum = -10
decimalMaximum = 10
decimalPlaces = 4

populationSize = 10


keys = []
for i in ('+','-','*','/','('):
    keys.append(i)

digits = []
for i in range(40,57):
    digits.append(str(chr(i)))

def randomDecimal():
    return round(random.uniform(decimalMinimum,decimalMaximum),decimalPlaces)

def assignKey():
    return bool(random.getrandbits(1))

def fillSpot():
    if assignKey():
        key = random.choice(keys)
        if key != '(':
            # Not paranthesis, means it's a mathimatical operator, so give two values.
            tmp = {}
            tmp[key] = []
            tmp[key].append(fillSpot())
            tmp[key].append(fillSpot())
        else:
            # Something's gotta go between the paranthesies, and we need a closing paranthesis also.
            tmp = []
            tmp.append('(')
            tmp.append(fillSpot())
            tmp.append(')')
        return tmp
    else:
        return randomDecimal()

def iterate(object):
    if isinstance(object,dict):
        for key, item in object.items():
            leftItem = item[0]
            rightItem = item[1]
            return str( iterate(leftItem) ) + str(key) + str( iterate(rightItem) )
    elif isinstance(object,list):
        tmp = ''
        for item in object:
            tmp = tmp + iterate(item)
        return tmp
    else:
        return str(object)


def evaluate(math):
    try:
        return eval(math)
    except:
        return False


def generatePopulation():
    population = []
    count = len(population)
    while True:
        tmp = fillSpot()
        if not isinstance(tmp,dict):
            continue
        if evaluate(iterate(tmp)):
            population.append(tmp)
            count = count + 1
            if count >= populationSize:
                break
    return population



population = generatePopulation()


for item in population:
    print ''
    print iterate(item)







