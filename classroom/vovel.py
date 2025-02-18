stri=open("vovel.txt","r")
out=open("output.txt","a")
string=stri.read()

vov=["a","e","i","o","u","A","E","I" ,"O","U"]
for i in string:
    if i in vov:
        out.write("#")
       
    else:
        out.write(i)