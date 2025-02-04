l=[]
n=int(input("Enter the number of list elements:"))
for i in range(n):
    l.append(int(input("Enter the list element:")))

print(l)
lar=max(l)
sma=min(l)
print("Largest number is:",lar)
print("Smallest number is:",sma)