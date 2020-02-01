# Third samister lab 1..

#Task 1,

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
        returnsum_numbers
        print(sum_list([1,2,-8]))

#Task 2


#Part 1,

list1 = ["2","6","7","8","1"]
print (list1)

#Part 2,

print("Smalest in he list =",min(list1))
print("Largest in the list =",max(list1))

#Part 3,

count =0
list = ["abc","xyz","aba","1221"]
for item in list:
    if len (item) >=2 and item [0] ==item[-1]:
        count +=1
        print("count",count)

#Part 4,

listted=[square**2 for square in range(1,31)]
print (" the first five  squared element in the list =" , listted [ : 5 ] )
print (" Tha last five squared element in the list =" , listted [-5 :] )

#Part 5,

shoping_list = []
while True :
    choice = input(" inter the item you want :")
    if not choice :
        break
    shoping_list.append(choice)
print (" Shoping list" ,shoping_list)

