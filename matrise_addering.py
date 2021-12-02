a = [[1, 2, 3, 4, 5], [3, 4, 5, 6, 7]]
b = [[2, 4, 6, 8, 9], [6, 8, 10, 12, 13]]


def matrise_adderer():
    if len(a) == len(b):
        for i in range(len(a)):
            for j in range(len(a[i])):
               b[i][j] += a[i][j]
    return b

print(matrise_adderer())