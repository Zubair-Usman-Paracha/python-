"""
def power(base,exp):
    if(exp==1):
        return(base)
    else:
        return (base*power(base,exp-1))
    
        
base=int(input("[*]Enter The base number:"))
exp=int(input("[*]The exponential value:"))
print("[=] Result :",power(base,exp))
"""

#bubble Sort
#selection sort

a = []
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element of List1 : " %i))
    a.append(value)

for i in range(number -1):
    for j in range(number - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp

print("The Sorted List in Ascending Order : ", a)
