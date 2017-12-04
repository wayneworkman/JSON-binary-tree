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

populationSize = 100

inputs = ['111','222','333','444','555','666']
expectedOutput = 1.21

keys = []
for i in ('+','-','*','/','('):
    keys.append(i)

digits = []
for i in range(40,57):
    digits.append(str(chr(i)))

def randomNumber():
    return random.uniform(0,100)

def randomDecimal():
    if randomBool():
        return round(random.uniform(decimalMinimum,decimalMaximum),decimalPlaces)
    else:
        return random.choice(inputs)

def randomBool():
    return bool(random.getrandbits(1))

def fillSpot():
    if randomBool():
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

def generatePopulation(population=None):
    if population is None:
        population = []
    count = len(population)
    while True:
        tree = fillSpot()
        if not isinstance(tree,dict):
            continue
        answer = evaluate(iterate(tree))
        if answer != False:
            item = {}
            item['tree'] = tree
            item['answer'] = answer
            count = count + 1
            population.append(item)
            if count >= populationSize:
                break
    return population

def gradeAnswer(answer):
    if answer > expectedOutput:
        return answer - expectedOutput
    else:
        return expectedOutput - answer

def gradePopulation(thePopulation):
    for item in thePopulation:
        if 'grade' not in item:
            item['grade'] = gradeAnswer(item['answer'])
    return thePopulation

def getGradeAverage(thePopulation):
    x = 0
    for item in thePopulation:
        x = x + item['grade']
    x = x / len(thePopulation)
    return x

def removeBelowAverage(thePopulation=None,theAverage=None):
    for item in thePopulation:
        if item['grade'] < theAverage:
            thePopulation.remove(item)
    return thePopulation

def getObjectDepth(object=None,depth=0):
    for item in object:
        depth = depth + 1
        getObjectDepth(item,depth)

def matePopulation(thePopulation):
    while len(thePopulation) < populationSize:
        leftParent = random.choice(thePopulation)['tree']
        rightParent = random.choice(thePopulation)['tree']
        child = {}
        # Get left half.

        # Get right half.



        answer = evaluate(iterate(child))
        if answer != False:
            child['tree'] = child
            child['answer'] = answer
            thePopulation.append(child)


while True:
    population = generatePopulation()
    population = gradePopulation(population)
    average = getGradeAverage(population)
    print 'Average score: ' + str(getGradeAverage(population))
    population = removeBelowAverage(thePopulation=population,theAverage=average)
    population = matePopulation(population)
























