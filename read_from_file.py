import traceback
def Read_From_File(path):
    try:
        msg=open(path).read()
        print(msg)
        return msg
    except:
        traceback.print_exc()
        return ''
