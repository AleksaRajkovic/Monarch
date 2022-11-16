import os,settings_obj,datetime
import random,string
def Create_File(settings,msg):
    os.chdir(settings.output_dir)
    name=Create_File_Name(settings)
    if(os.path.isfile(name)):
        print('Error! File already exists!')
    else:
        file = open(name+'.txt', 'w')
        file.write(msg)
    return name


def Create_File_Name(settings):
    if(settings.datetime==True):
        dt=' - '+str(datetime.datetime.now()).replace('.','-').replace(':','-')
    else:
        dt=''
    if(settings.rng==True):
        rng=NameGen(settings)
    else:
        rng=''
    name=settings.prefix+rng+dt+settings.suffix
    return name

def choice():
    return str(random.randint(0,1))
def randNum():
    return str(random.randint(0,9))
def randLetter():
    return random.choice(string.ascii_letters)
def NameGen(settings):
    dict={
    '0':randNum,
    '1':randLetter
    }
    name=''
    for i in range(settings.len):
        name+=dict[choice()]()
    
    return name


