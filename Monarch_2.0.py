import get_tables 
import load_settings
import settings_obj
import encryption,decryption
import cipher_generator
import re
import os
import write_to_file
import read_from_file
import traceback
import utility
tables,dec_tables=get_tables.CreateTables()
general_settings,naming_settings=load_settings.LoadSettings()
settings=settings_obj.Settings(general_settings,naming_settings)
msg=''
while(True):
    com=input('>>')
    if(re.search('in/',com,re.IGNORECASE)):
        msg=com.split('/')[1]
    if(re.search('rff/',com,re.IGNORECASE)):
        msg=read_from_file.Read_From_File(com.split('/')[1])
    elif(re.search('enc/',com,re.IGNORECASE)):
        msg=encryption.Encrypt(settings,tables,msg)
        if(settings.auto_print==True):
            print(msg)
    elif(re.search('dec/',com,re.IGNORECASE)):
        msg=decryption.Decrypt(settings,dec_tables,msg)
        if(settings.auto_print==True):
            print(msg)
    elif(re.search('gen/',com,re.IGNORECASE)):
        for i in range(settings.cipher_gen_count):
            print(cipher_generator.GenerateCipher(int(com.split('/')[1])))
    elif(re.search('print',com,re.IGNORECASE)):
        print(msg)
    elif(re.search('wtf/',com,re.IGNORECASE)):
        print('File Created! ',write_to_file.Create_File(settings,msg))
    elif(re.search('cls',com,re.IGNORECASE) or re.search('clear',com,re.IGNORECASE)  ):
        utility.clearConsole()
    elif(re.search('com/',com,re.IGNORECASE)):
        print(open(os.path.abspath('commands.txt'),'r').read())




