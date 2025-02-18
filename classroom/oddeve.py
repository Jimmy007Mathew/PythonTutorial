f=open("number.txt","r")
number=f.read()
a=number.split()
print(a)
od=open("odd.txt","a")
ev=open("eveen.txt","a")
for i in a:
    if(int(i)%2==0):
        ev.write(i+" ")
    else:
        od.write(i+" ")