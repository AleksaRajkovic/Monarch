import get_tables
import random
def GenerateCipher(sub_length):
    numbers=[]
    cipher=''
    length=len(get_tables.GetChars())
    counter=0
    while(counter<length):
        number=GenerateNumber(sub_length)
        if(number not in numbers):
            numbers.append(number)
            counter+=1
    for n in numbers:
        cipher+=n
    cipher=f'SUB_LENGTH({sub_length}):'+cipher
    return cipher

def GenerateNumber(sub_length):
    number=''
    for i in range(sub_length):
       number+=str(random.randint(0,9))
    return number
