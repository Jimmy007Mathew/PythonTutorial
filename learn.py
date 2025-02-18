st=input("Enter the string:")
key= int(input("Enter the key:"))
enst=""
for ch in st:
    ordch=ord(ch)+key
    if(ordch>ord("z")):
       ordch= ord("a")+(ordch-ord("z")-1)
    enst+=chr(ordch)
print(enst)
