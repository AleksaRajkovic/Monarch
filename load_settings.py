import os
def LoadSettings():
    general_settings={}
    naming_settings={}
    settings=open(os.path.abspath(r'settings.txt'),'r').read().split('\n')
    settings.remove(settings[0])
    index=settings.index('	--NAMING_SETTINGS--')
    for i in range(len(settings)):
        split=settings[i].split('=')
        if(i<index):
            try:
                general_settings[split[0]]=split[1]
            except:
                pass
        else:
            try:
                naming_settings[split[0]]=split[1]
            except:
                pass
    return general_settings,naming_settings




