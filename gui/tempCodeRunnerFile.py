
        file3.write(line)  # Keep the line as is
       # file4.write('H^' + s[1]+ '^00' + s[3] +str(leng(startadd))+'\n')
    else:
        if s[2] == 'RESW' or s[2] == 'RESB' or s[2]=='RESD' or  s[2] == 'END':
            # Before handling RESW/RESB, write any remaining records to the file
            if len(stack) > 0: