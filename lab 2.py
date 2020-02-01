
# Task 1
def addMatrix(m1,m2):
    finalmatrix = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            finalmatrix[i][j] = m1[i][j] + m2[i][j]
    return finalmatrix
matrix1=eval(input("Enter first matrix:"))
matrix2=eval(input("Enter second matrix:"))
matrix=addMatrix (matrix1,matrix2)
print(matrix)

# Task 2
n= int(input("Enter n number:"))
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n -i -1] = '*'
for row in a:
    print(' ' . join(row))


# Task 3
m, n = [int(k) for k in input().split()]
A = [[int(k) for k in input() .split()] for i in range(m)]
c = int(input())

for i in range(m):
    for j in range(n):
        A[i][j] *= c

print('\n'.join([' '.join([str(k) for k in row]) for row in A]))

#Class task..

class stack:
    def __init__(self,a):
        self.a=a
    def push(self,index,value):
        self.a.insert(index,value)
    def pop(self,index):
        return self.a.pop(index)
    def __str__(self):
        return str(self.a)
l=[1,2,3]
print(l)
List1=stack(l)
List1.push(2,33)
List1.pop(1)
print(List1)


















