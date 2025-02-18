symtab = {}
with open('symtab.txt', 'r') as f:
    for line in f:
        label, address = line.split()
        if label in symtab:
            print(f"Duplicate label: {label}")
            break
        symtab[label] = address

optab = {}
with open('optab.txt', 'r') as f:
    for line in f:
        mnemonic, opcode = line.split()
        optab[mnemonic] = opcode

file2 = open('intermediate.txt', 'r')
file3 = open('out.txt', 'w')
file4 = open('record.txt', 'w')
Text=''
global tc
tc=0x0001
stack=[]

def record(opc):
    if(len(stack)<11):
            stack.append(opc)
    Text='T^00'+startadd+'^'+hex(tc)+'^'
    for i in stack:
        Text+=i
    file4.write(Text+'\n')
    stack.clear()
    stack.append(opc)
    tc=0
        
    
for line in file2:
    s = line.split()
    if s[2] == 'START':
        startadd=s[3]
        file3.write(line)  # Keep the line as is
        file4.write('H^' + s[2] +'00'+s[3] +'\n')
    else:
        if s[2] == 'RESW' or s[2] == 'RESB' or s[2] == 'END':
            file3.write(line)  # Keep the line as is
        elif s[2] == 'WORD':
            file3.write(line.strip() + ' 00' + s[0][2:] + '\n')
            record('00'+s[0][2:])
        elif s[2] == 'BYTE':
            file3.write(line.strip() + ' ' + s[3][2:] + '\n')
            record(s[3][2:])
        else:
            if s[3] in symtab:
                file3.write(line.strip() + ' ' + optab[s[2]] + symtab[s[3]][2:] + '\n')
                temp=optab[s[2]] + symtab[s[3]][2:]
                record(temp)
            else:
                file3.write(line.strip() + ' ' + optab[s[2]] + '0000\n')
                temp=optab[s[2]] + '0000'
                record(temp)

file4.write('E^00' + startadd)
s
file2.close()
file3.close()
