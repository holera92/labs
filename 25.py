import random
import math
from typing import List

def IsSorted(array: list, ascending = True) -> bool:
    if ascending:
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                return False
    else: 
        for i in range(1, len(array)):
            if array[i-1] < array[i]:
                return False
    return True

def BozoSort(array: list, ascending = True) -> List[int]:

    result = []

    if len(array) <= 1:
        return result

    if type(array[0]) == list:
        for row in array:
            result += row
    else:
        result = array.copy()

    while not IsSorted(result, ascending):
        a, b = random.randint(0, len(result)-1), random.randint(0, len(result)-1)
        result[a], result[b] = result[b], result[a]

    return result


def BozoSortForThree(a: int, b: int, c: int, ascending = True) -> List[int]:
    return BozoSort([a, b, c], ascending)





n = int(input())
n_sqrt = int(n**0.5)

vector = list(map(int, input().split(' ')))
matrix = []
row = []
i = 0
for elem in vector:
    row.append(elem)
    i += 1
    if (i % n_sqrt == 0):
        matrix.append(row)
        row = []
        i = 0
del row, i



print(' '.join(map(str, BozoSort(vector, True))))
print(' '.join(map(str, BozoSort(vector, False))))
print(' '.join(map(str, BozoSort(matrix, True))))
print(' '.join(map(str, BozoSort(matrix, False))))
print(' '.join(map(str, BozoSortForThree(vector[0], vector[1], vector[2], True))))
print(' '.join(map(str, BozoSortForThree(vector[0], vector[1], vector[2], False))))
