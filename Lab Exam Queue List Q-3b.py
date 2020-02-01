print ("Name : Zubair Usman ")
print ("Reg no : 13763")
print ("Final term Lab Exam ...")

print ("--------------- ( Queue List ) ---------------")
def checkInt(elements):
	for element in elements:
		if element.__class__ == int:
			print(element)

# b. Functions to calculate the sum, product of a list. 
def sum(elements):
	add = 0
	for element in elements:
		if element.__class__ == int:
			add+=element
	return add
def product(elements):
	mul = 1
	for element in elements:
		if element.__class__ == int:
			mul*=element
	return mul

# c. Function to calculate the maximum and its position.
def maximum(elements):
	max = elements[0]
	index = 0
	for element in elements:
		if element.__class__ == int:
			if max < element:
				max = element
	return max,elements.index(max)

# d. Function to find if an element x belongs to a list.	 
def inList(element,elements):
	return element in elements

elements = [1,2,'3',5,'1',6,9]
print(elements)
print("Check Integers:")
checkInt(elements)
print("[+]Sum of the Queue:")
print(sum(elements))
print("[=]Product of the Queue:")
print(product(elements))
print("[::]Maximum (element, index):")
print(maximum(elements))
print("[=]checking whether 2 in List:")
print(inList(2,elements))
