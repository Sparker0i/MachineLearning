import csv
import numpy as np

def loop(m , c , dataset , a):
    cj = 0
    mj = 0
    N = len(dataset)
    N = float(N)
    for i in range(len(dataset)):
        x = dataset[i , 0]
        y = dataset[i , 1]
        cj -= (1/N) * (y - ((m * x) + c))
        mj -= (1/N) * (y - ((m * x) + c)) * x
    return [c - (a * cj) , m - (a * mj)]

def compute_error(c, m, dataset):
    totalError = 0
    for i in range(0, len(dataset)):
        x = dataset[i, 0]
        y = dataset[i, 1]
        totalError += (y - (m * x + c))
    return totalError / float(len(dataset))

def gradientDescent(dataset):
    m = 0
    c = 0
    a = 0.001
    n = len(dataset)
    for i in range(n):
        [m , c] = loop(m , c , dataset , a)
    return [m , c]

dataset = np.genfromtxt('D1.csv' , delimiter=",")
c = 0
m = 0
print compute_error(c , m , dataset)
[m , c] = gradientDescent(dataset)
print m,
print c
print compute_error(c , m , dataset)
