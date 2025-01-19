st=input("Enter the string:")
print("ENCRYPTION\n")
key= int(input("Enter the key:"))
encst=""
for ch in st:
    ordch=ord(ch)+key
    if(ord("Z")<ordch<ord("a")):
        ordch= ord("A")+(ordch-ord("Z")-1)
    elif(ordch>ord("z")):
       ordch= ord("a")+(ordch-ord("z")-1)
    encst+=chr(ordch)
print("\nEncrypted String:",encst)

print("DECRYPTION\n")

decst=""
for ch in encst:
    ordch=ord(ch)-key
    if(ord("Z")<ordch<ord("a")):
        ordch=ord("z")-(ord("a")-ordch-1)
    elif(ordch<ord("A")):
        ordch=ord("Z")-(ord("A")-ordch-1)
    decst+=chr(ordch)
print("\nDecrypted String:",decst)


