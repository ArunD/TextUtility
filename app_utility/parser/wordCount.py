import os
import io
class TextParser:

    #def __init__(self, tmp_dir):
    #    self.tmp_dir = tmp_dir

    def parse(self,datatype,document,charList=[]):
        if datatype =='file':
            f = open(document,'r') #file
        else:
            f = io.StringIO(document) #text stream
        #print(type(f))
        wcl = {}
        t = []
        nl = 0
        l = 0
        wc = 0
        tu = []
        for line in f:
            #print(line)
            nl += 1
            if(not (line.startswith('\n') or line.startswith(' \n') )):
                l += 1
                t = line.strip('\n').split(' ')
                for w in t:
                    wc += 1
                    if w in wcl:
                        wcl[w] += 1
                    else :
                        wcl[w] = 1

        
        f.close()
        #print(wcl)

        for k,v in wcl.items():
            tu.append((k,v))

        stu = sorted(tu,key=lambda wv : wv[1],reverse=True)

        return({'nl' : nl , 'l' : l , 'wc' : wc , 'tu' : stu})

    