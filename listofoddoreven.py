s= input("Enter the list of number:")
x= list(s)
even=[]
odd=[]
for i in x :
    if i%2==0:
        even.append(i)
    else:
         odd.append(i)
print(odd)
print(even)
