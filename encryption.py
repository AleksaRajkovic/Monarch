import re
import settings_obj
import traceback
import fake_hex
def Encrypt(settings,tables,msg):
    for i in range(settings.enc_levels):
        msg=Encryption_Layer(settings,tables[int(settings.order[i])],msg)
    msg=fake_hex.FakeHex(settings,msg)
    return msg

def Encryption_Layer(settings,table,msg):
    msg_to_list=re.findall('.',msg)
    encrypted_msg=''
    for char in msg_to_list:
        try:
            encrypted_msg+=table[char]
        except:
            traceback.print_exc()
    return encrypted_msg
