import re
import settings_obj
import traceback
import fake_hex
def Decrypt(settings,dec_tables,msg):
    msg=fake_hex.RemoveHex(msg)
    for i in range(settings.enc_levels):
        msg=Decryption_Layer(settings,dec_tables[int(list(reversed(settings.order))[i])],msg)
    return msg

def Decryption_Layer(settings,dec_table,msg):
    length=len(list(dec_table.keys())[1])
    msg_to_list=re.findall('.'*length,msg)
    decrypted_msg=''
    for num in msg_to_list:
        try:
            decrypted_msg+=dec_table[num]
        except:
            traceback.print_exc()

    return decrypted_msg
