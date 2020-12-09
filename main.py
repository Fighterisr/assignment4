import sympy as sp
import mpmath as mp

def bisectionMethod(polynomial, startPoint, endPoint, epsilon):
    error = -(mp.ln((epsilon)/(endPoint-startPoint))/(mp.ln(2)))
    iteration = 0
    middlePoint = 0
    while endPoint - startPoint > epsilon:
        middlePoint = (startPoint + endPoint) / 2
        if polynomial(startPoint)*polynomial(middlePoint) < 0:
            endPoint = middlePoint
        else:
            startPoint = middlePoint
        iteration += 1
    return middlePoint

def findRoots(polynomial, startPoint, endPoint, segmentLength):
    roots = []
    originalStartPoint = startPoint
    while startPoint < endPoint:
        if polynomial(startPoint)*polynomial(startPoint + segmentLength) < 0:
            root = bisectionMethod(polynomial,startPoint,startPoint + segmentLength, 10**-10)
            roots.append(root)
        startPoint += segmentLength
    x = sp.symbols('x')
    derivative = sp.diff(polynomial(x), x)
    derivative = sp.lambdify(x, derivative, 'math')
    startPoint = originalStartPoint
    while startPoint < endPoint:
        if derivative(startPoint)*derivative(startPoint + segmentLength) < 0:
            root = bisectionMethod(derivative, startPoint, startPoint + segmentLength, 10**-10)
            if(mp.almosteq(polynomial(root),0)):
                roots.append(root)
        startPoint += segmentLength
    print('The roots of', polynomial(x), 'are:')
    [print('Root number', str(index + 1) + ':', value) for index, value in enumerate(roots)]

polynomial = lambda x: x**4+x**3-3*x**2



findRoots(polynomial,-3,2,0.1)

