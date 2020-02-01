
def Insertion_Sort(A):
    for i in range(0,len(A)):
        j = i-1
        while j>=0 and A[j+1]< A[j]:
            A[j],A[j+1]=A[j+1],A[j]
            j=j-1
A=[10,5,9,3,7,2,1,4,6,8]
print(A)
print("Insertion")
Insertion_Sort(A)
print(A)
