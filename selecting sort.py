A = [10 ,12 ,13,9,2,8,58,6,382]

for i in range (len(A)):

    minimum = i

    for j in range (i+1 , len(A)):
        if A [minimum] > A[j]:

            minimum = j

    A [i] , A [minimum] = A [minimum] , A[i]

print ("sorted list")

for i in range (len(A)):
    
    print ("[+]%d" %A[i])

