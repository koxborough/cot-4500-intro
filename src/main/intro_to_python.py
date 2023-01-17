import numpy as np
import sys

LENGTH = 3

def task_1(matrix: list):
    for i in range (len(matrix)):
      for j in range(len(matrix[i])):
          matrix[i][j] = 1 if (i == j) else 0

def task_2(matrix: list):
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
          if (i != j):
              matrix[i][j] = matrix[i][j] + 3

def task_3(matrix: list):
    for i in range(len(matrix)):
        matrix[i].pop(len(matrix[i]) - 1)

def print_matrix(matrix: list, newline: bool):
    print(np.matrix(matrix), "\n" if (newline) else "")

matrix = [[0 for i in range(LENGTH)] for j in range(LENGTH)]

task_1(matrix)
print_matrix(matrix, True)

task_2(matrix)
print_matrix(matrix, True)

task_3(matrix)
print_matrix(matrix, False)