import os
import re
def CreateTables():
    tables={}
    dec_tables={}
    chars=GetChars()
    subs=GetSubs(chars)
    for x in range(len(subs)):
        table={}
        dec_table={}
        for i in range(len(chars)):
            table[chars[i]]=subs[x][i]
            dec_table[subs[x][i]]=chars[i]
        tables.update({x:table})
        dec_tables.update({x:dec_table})
    return tables,dec_tables

def GetChars():
    return open(os.path.abspath(r'chars.txt'),'r').read()
    
   
def GetSubs(chars):
    sub_tables=[]
    subs=open(os.path.abspath(r'subs.txt'),'r').read().strip().split('\n')
    for i in range(len(subs)):
        temp_sub=subs[i].split(':')
        sub_len=int(temp_sub[0].split(')')[0].replace('SUB_LENGTH(',''))
        if(len(temp_sub[1])/sub_len !=len(chars)):
            print("Error! Sub length and number of chars don't match!")
        else:
            sub_tables.append(re.findall('.'*sub_len,temp_sub[1]))
    print(len(sub_tables),'Tables loaded.')
    return(sub_tables)
            