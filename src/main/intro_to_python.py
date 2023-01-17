import numpy as np

# We have a "constant" length of 3 for the size of the matrix
LENGTH = 3

# Sets the indices of equal row and column numbers to 1 and every other element 0
def task_1(matrix: np.ndarray):
    for i in range (len(matrix)):
      for j in range(len(matrix[i])):
          matrix[i][j] = 1 if (i == j) else 0

# Adds 3 to every element where row and column numbers do not equal
def task_2(matrix: np.ndarray):
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
          if (i != j):
              matrix[i][j] = matrix[i][j] + 3

# Deletes last row of matrix
def task_3(matrix: np.ndarray):
    matrix_temp = np.delete(matrix, len(matrix[0]) - 1, 1)
    return matrix_temp

# Print out the matrix
def print_matrix(matrix: np.ndarray, newline: bool):
    for i in range(len(matrix)):
        columnLength = len(matrix[i])
        for j in range(columnLength):
            print(int(matrix[i][j]), end=(" " if (j != columnLength - 1) else "\n"))
    if (newline):
        print()

if __name__ == "__main__":
    matrix = np.zeros((LENGTH, LENGTH))

    task_1(matrix)
    print_matrix(matrix, True)

    task_2(matrix)
    print_matrix(matrix, True)

    matrix = task_3(matrix)
    print_matrix(matrix, False)