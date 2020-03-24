s= input("Enter the list of number:")
x= list(s)
even=[] #  defining empty list
odd=[] # defining empty list 
for i in x :
    if i%2==0:
        even.append(i) # if the condition is true then using append method number adds to  even  list everytime.
    else:
         odd.append(i)  # if the condition is false then using append method number adds to  odd  list everytime.
print(odd)
print(even)
