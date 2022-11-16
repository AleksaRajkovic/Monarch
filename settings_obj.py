import re
class Settings:
    def __init__(self,general_settings,naming_settings):
        self.output_dir = general_settings['OUTPUT_DIR']
        self.enc_levels = int(general_settings['ENCRYPTION_LEVELS'])
        self.order=Cut(ToList(general_settings['ORDER_OF_TABLES']),self.enc_levels)
        self.fake_hex=ToBool(general_settings['FAKE_HEX'])
        self.scramble=ToBool(general_settings['SCRAMBLE'])
        self.scramble_levels=int(general_settings['SCRAMBLE_LEVELS'])
        self.scramble_order=ToList(general_settings['SCRAMBLE_ORDER'])
        self.auto_print=ToBool(general_settings['AUTO_PRINT'])
        self.auto_wtf=ToBool(general_settings['AUTO_WRITE_TO_FILE'])
        self.cipher_gen_count=int(general_settings['CIPHER_GEN_COUNT'])
        self.log_path=naming_settings['LOG_PATH']
        self.log=ToBool(naming_settings['LOG'])
        self.datetime=ToBool(naming_settings['DATETIME'])
        self.len=int(naming_settings['LENGTH'])
        self.prefix=naming_settings['PREFIX']
        self.suffix=naming_settings['SUFFIX']
        self.rng=ToBool(naming_settings['RANDOM_GEN'])
def ToBool(string):
    if(re.search('TRUE',string,re.IGNORECASE)):
        return True
    else:
        return False
def ToList(string):
    return string.strip().split(',')
def Cut(list,len):
    newlist=[]
    for i in range(len):
        newlist.append(list[i])
    return newlist



            