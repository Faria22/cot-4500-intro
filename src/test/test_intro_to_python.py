import numpy as np

def printArr(arr):
    for r, row in enumerate(a):
        s = ''
        for c, column in enumerate(row):
            s += f'{arr[r, c]} '
        print(s)

a = np.array([[0, 0, 0], [0, 0, 0], [ 0, 0, 0]])

for r, row in enumerate(a):
    for c, column in enumerate(row):
        if r == c:
            a[r, c] = 1

printArr(a)
print()

for r, row in enumerate(a):
    for c, column in enumerate(row):
        if r != c:
            a[r, c] = a[r, c] + 3

printArr(a)
print()

a = np.hsplit(a, 3)

a = np.concatenate((a[0], a[1]), axis=1)
printArr(a)
