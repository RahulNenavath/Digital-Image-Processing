def Matrix_input():

  matrix = []

  print('Enter the elements row wise: ')

  # 5 x 5 Matrix input:
  for i in range(0,5):
    
    row = []
    
    for j in range(0,5):
      e = int(input())
      row.append(e)

    matrix.append(row)
  
  return matrix


def display_matrix(A):
  for i in range(0,5):
    for j in range(0,5):
      print(A[i][j], end=" ")
    print()
   

def sort_Matrix(A):
  k = 0
  size = len(A)
  temp = [0]*(size*size)
  
  for i in range(0,5):
    for j in range(0,5):
      temp[k] = A[i][j]
      k = k + 1
  
  temp.sort()

  k = 0
  
  for i in range(0,5):
    for j in range(0,5):
      A[i][j] = temp[k]
      k = k+1

  return A

def sum_matrix(A):
  Sum = 0
  for i in range(0,5):
    for j in range(0,5):
      Sum = Sum + A[i][j]

  return Sum

def Max_matrix(A):
  A = sort_Matrix(A)

  return A[4][4]


def Mean_matrix(A):
  s = sum_matrix(A)
  return s / len(A)**2


def Median_matrix(A):
  k = 0
  size_M = len(A) * len(A)
  A = sort_Matrix(A)
  temp = [0]*(size_M)
  for i in range(0,5):
    for j in range(0,5):
      temp[k] = A[i][j]
      k = k + 1

  if (size_M % 2 == 0):
    median_1 = temp[size_M//2]
    median_2 = temp[size_M//2-1]
    median = (median_1 + median_2)/2
    return temp[median]

  else:
    return temp[size_M//2]
    

def Mode_matrix(A):
  k = 0
  size = len(A)
  temp = [0]*(size*size)
  
  for i in range(0,5):
    for j in range(0,5):
      temp[k] = A[i][j]
      k = k + 1
  
  most = max(list(map(temp.count, temp)))
  return list(set(filter(lambda x: temp.count(x) == most, temp)))


def SD_matrix(A):
  k = 0
  size = len(A) * len(A)
  temp = [0]*(size)
  for i in range(0,5):
    for j in range(0,5):
      temp[k] = A[i][j]
      k = k + 1

  mean = Mean_matrix(A)

  sum = 0
  for x in temp:
    i = (x - mean)**2
    sum = i + sum
  
  l = sum / size 

  return l**(1/2)


A = Matrix_input()

display_matrix(A)

A = sort_Matrix(A)

print('Sorted Matrix: ')
print('----------------------------')

display_matrix(A)

Total = sum_matrix(A) 

max_el = Max_matrix(A) 

mean = Mean_matrix(A)

median = Median_matrix(A)

mode = Mode_matrix(A)

stD = SD_matrix(A)

print('----------------------------')
print('1. Sum: {}, 2.Max: {}, 3.Mean: {}, 4.Median: {}, 5.Mode: {}, Standard Deviation: {}'.format(Total,max_el,mean,median,mode,stD))
  
