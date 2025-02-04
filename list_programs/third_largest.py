l=[]
n=int(input("Enter the number of list elements:"))
for i in range(n):
    l.append(int(input("Enter the list element:")))

co=0
ma=max(l)
while(ma in l):
    l.remove(ma)
    if ma not in l and co<1:
        ma=max(l)
        co+=1

print("Thirs largest element is ",l[-1])