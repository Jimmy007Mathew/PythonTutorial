l1=[]
n=int(input("Enter the number of elements for list 1:"))
for i in range(n):
    l1.append(int(input("Enter the list element:")))

l2=[]
n=int(input("Enter the number of elements for list 2:"))
for i in range(n):
    l2.append(int(input("Enter the list element:")))

l3=[]

for i in l1:
    if i in l2:
        l3.append(i)

print("List 1:",l1)
print("List 2:",l2)
print("List 3:",l3)