import os
import re
import string
class SpecialCharParser:

    #def __init__(self, tmp_dir):
    #    self.tmp_dir = tmp_dir

    def parse(self,datatype,document,charList):
        #print(document)
        legal_chars =  string.ascii_letters + string.digits
        legal_chars = '[^%s\n]+' % re.escape(legal_chars)

        if datatype =='file':
            f = open(document,'r')
            c = f.read()
            #print(c)
            l = re.findall(legal_chars,c)
            f.close()
        else:
            l = re.findall(legal_chars,document)
        
        s = ' '.join(set(l))

        return({'specialChar' : s})

        