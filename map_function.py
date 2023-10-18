'''
map function...basic uses
'''
#EXAMPLE 1: Using map function to double every element in the list
list_x = [1,2,3,4,5,6,7,8,9,10]

def double_it(item):
	return item * 2

result = map(double_it, list_x) 
print("Doubled list:", list(result)) #map() returns a map object so we send it to a list


#EXAMPLE 2: Turning all the list items into even numbers without using map()
list_b = [37,253,68,40,24,99,71]

def make_even(element):
	if element % 2 == 0:
		return element   
	else:
		return element + 1  

list_bb = []

for i in list_b:
	list_bb.append(make_even(i))

print("New list list_bb:", list_bb)


#EXAMPLE 3: Using map function to turn all the list items into even numbers
#NOTE: Using map() results into lesser LOC and is more concise
list_b = [37,253,68,40,24,99,71]

def make_even(element):
	if element % 2 == 0:
		return element   
	else:
		return element + 1  

result = map(make_even, list_b)
print("Even numbers:", list(result))
