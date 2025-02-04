l=[]
n=int(input("Enter the number of list elements:"))
for i in range(n):
    l.append(int(input("Enter the list element:")))

num=int(input("Enter the number:"))
newl=[]
for i in l:
    if i<num:
        newl.append(i)

print("old list:",l)
print("new List:",newl)
