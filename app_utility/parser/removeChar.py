import os
import re
import string
import io
class RemoveCharParser:

    def __init__(self, charList):
        self.charList = charList

    def parse(self,datatype,document):

        pattern = '\r'
        carriage = "\r"
        newLine = "\n"
        space = "\s"
        tab = "\t"

        pattern = ''.join(self.charList)
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

        