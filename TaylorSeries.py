from math import pow, factorial , cos
import matplotlib.pyplot as plt

"""
:param angle: angle in radians
:param terms: number of terms to include in taylor expansion
:returns: result of evaluation of cos(angle) using Taylor series with given terms
"""
def taylorCos(angle, terms):
    result = 0
    for i in range(terms):
        result += pow(-1, i) * pow(angle, 2*i) / factorial(2*i)
    return result

def arithmeticSequence(start, incr, terms):
    result = []
    for i in range(terms):
        result.append(start + incr*i)
    return result

def generateSamples(low, high, count):
    incr = (high - low) / (count - 1)
    return arithmeticSequence(low, incr, count)

def plotRealCosVersusComputed(low, high, number, taylorN):
    angles = generateSamples(low, high, number)
    realCosList = []
    myCosList = []
    for value in angles:
        realCosList.append(cos(value))
        myCosList.append(taylorCos(value, taylorN))
    plt.plot(angles, realCosList, 'red')
    plt.plot(angles, myCosList, 'blue')
    plt.xlabel('Angle values')
    plt.ylabel('Cos(angle)')
    plt.show()
        
        
