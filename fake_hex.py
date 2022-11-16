import settings_obj
import re
import random
import traceback
def FakeHex(settings,msg):
    if(settings.fake_hex==False):
        return msg
    else:
        new_msg=''
        msg_list=re.findall('.',msg)
        hex_letters=re.findall('.','ABCDEF')
        for i in range(len(msg)):
            new_msg+=msg[i]
            chance=random.randint(0,10)
            if(chance>2 and chance<7):
                letter=random.randint(0,5)
                try:
                    new_msg+=hex_letters[letter]
                except:
                    traceback.print_exc()
            
        
        return new_msg
def RemoveHex(msg):
    hex_letters='ABCDEF'
    new_msg=''
    for char in msg:
        if(char not in hex_letters):
            new_msg+=char
    return new_msg



    



