l=[]
n=int(input("Enter the number of list elements:"))
for i in range(n):
    l.append(int(input("Enter the list element:")))

newl=[]
for i in l:
    if(i%2==0):
        newl.append(i)
newl.sort()
print("old list:",l)
print("new list:",newl)