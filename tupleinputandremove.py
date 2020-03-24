s= input("Enter some numbers with seperated")
x=tuple(s) # converting input to Tuple
type(x)
print(x)
y=list(x) # converting tuple to List
print(y)
y.pop(0) # remvoing first element using pop method in list
print(y)
y.pop() # removing last element using pop method in list. If we don't specify the position of the element it defaultly deletes last element.
print(y)
x=tuple(y) # converting list to Tuple
print(x)
