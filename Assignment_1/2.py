# 2nd Question:

import random as rnd

R = int(input('Number of Rows: '))
C = int(input('Number of Columns: '))

def Matrix_input(R,C):

  print('Matrix with Random Numbers Generated')

  matrix = []

  # 5 x 5 Matrix input:
  for i in range(0,R):
    
    row = []
    
    for j in range(0,C):
      e = rnd.randrange(0,100)
      row.append(e)

    matrix.append(row)
  
  return matrix

def display_matrix(A,R,C):

  for i in range(0,R):
    for j in range(0,C):
      print(A[i][j], end=" ")
    print()
   
def sort_Matrix(A,R,C):
  k = 0
  size_M = R * C
  temp = [0]*(size_M)
  
  for i in range(0,R):
    for j in range(0,C):
      temp[k] = A[i][j]
      k = k + 1
  
  temp.sort()

  k = 0

  for i in range(0,R):
    for j in range(0,C):
      A[i][j] = temp[k]
      k = k+1

  return A

def sum_matrix(A,R,C):
  Sum = 0
  for i in range(0,R):
    for j in range(0,C):
      Sum = Sum + A[i][j]

  return Sum


def Max_matrix(A,R,C):
  A = sort_Matrix(A,R,C)

  return A[R-1][C-1]

def Mean_matrix(A,R,C):
  s = sum_matrix(A,R,C)
  return s / (R * C)

def Median_matrix(A,R,C):
  k = 0
  # size_M = len(A) * len(A)
  size_M = R * C
  temp = [0]*(size_M)
  for i in range(0,R):
    for j in range(0,C):
      temp[k] = A[i][j]
      k = k + 1
  
  temp.sort()

  if (size_M % 2 == 0):
    median_1 = size_M//2
    median_2 = size_M//2-1
    median = (median_1 + median_2)/2
    return temp[int(median)]

  else:
    return temp[int(size_M//2)]

def Mode_matrix(A,R,C):
  k = 0
  size_M = R * C
  temp = [0]*(size_M)
  
  for i in range(0,R):
    for j in range(0,C):
      temp[k] = A[i][j]
      k = k + 1
  
  most = max(list(map(temp.count, temp)))
  x = list(set(filter(lambda x: temp.count(x) == most, temp)))

  if len(x) == len(temp):
    return 0
  else:
    return x


def SD_matrix(A,R,C):
  k = 0
  size_M = (R * C)
  temp = [0]*(size_M)
  for i in range(0,R):
    for j in range(0,C):
      temp[k] = A[i][j]
      k = k + 1

  mean = Mean_matrix(A,R,C)

  sum = 0
  for x in temp:
    i = (x - mean)**2
    sum = i + sum
  
  l = sum / size_M 

  return l**(1/2)



A = Matrix_input(R,C)

print('{} x {} Matrix: '.format(R,C))
print('----------------------------')

display_matrix(A,R,C)

A = sort_Matrix(A,R,C)

print('Sorted Matrix: ')
print('----------------------------')

display_matrix(A,R,C)

Total = sum_matrix(A,R,C)

max_el = Max_matrix(A,R,C)

mean = Mean_matrix(A,R,C)

median = Median_matrix(A,R,C)

mode = Mode_matrix(A,R,C)

stD = SD_matrix(A,R,C)

print('----------------------------')
print('1. Sum: {}, 2.Max: {}, 3.Mean: {}, 4.Median: {}, 5.Mode: {}, Standard Deviation: {}'.format(Total,max_el,mean,median,mode,stD))






