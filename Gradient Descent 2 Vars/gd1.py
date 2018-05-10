import csv
import numpy as np

def loop(m1 , m2 , c , dataset , a):
    cj = 0
    m1j = 0
    m2j = 0
    N = len(dataset)
    N = float(N)
    for i in range(len(dataset)):
        x1 = dataset[i , 0]
        y = dataset[i , 1]
        x2 = dataset[i , 2]
        cj -= (1/N) * (y - ((m1 * x1) + (m2 * x2) + c))
        m1j -= (1/N) * (y - ((m1 * x1) + (m2 * x2) + c)) * x1
        m2j -=(1/N) * (y - ((m1 * x1) + (m2 * x2) + c)) * x2
    return [c - (a * cj) , m1 - (a * m1j) , m2 - (a * m2j)]

def compute_error(c, m1, m2 , dataset):
    totalError = 0
    for i in range(0, len(dataset)):
        x1 = dataset[i, 0]
        y = dataset[i , 1]
        x2 = dataset[i, 2]
        totalError += (y - (m1 * x1 + m2 * x2 + c))
    return totalError / float(len(dataset))

def gradientDescent(dataset):
    m1 = 0
    m2 = 0
    c = 0
    a = 0.001
    n = len(dataset)
    for i in range(n):
        [c , m1 , m2] = loop(m1 , m2 , c , dataset , a)
    return [m1 , m2 , c]

dataset = np.genfromtxt('D2.csv' , delimiter=",")
c = 0
m1 = 0
m2 = 0
print compute_error(c , m1 , m2 , dataset)
[m1 , m2 , c] = gradientDescent(dataset)
print m1,
print m2,
print c
print compute_error(c , m1 , m2 , dataset)
