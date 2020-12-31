import os
import re
import string
import io
class RemoveCharParser:

    #def __init__(self, tmp_dir):
    #    self.tmp_dir = tmp_dir

    def parse(self,datatype,document,charList):

        pattern = '\r'
        carriage = "\r"
        newLine = "\n"
        space = "\s"
        tab = "\t"

        pattern = ''.join(charList)
        pattern = pattern + "\r"
        pattern = '[%s]+' % pattern
        #legal_chars = '[^%s\s\n]+' % re.escape(legal_chars)
                
        if datatype =='file':
            f = open(document,'r')
            c = f.read()
            op = re.sub(pattern,r'',c)
            f.close()
        else:
            op = re.sub(pattern,r'',document)

        
        return({'removeChar' : op})

        