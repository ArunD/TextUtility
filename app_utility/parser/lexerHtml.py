from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

#lexer = get_lexer_by_name("python", stripall=True)
#formatter = HtmlFormatter(full="true")

class LexerOp:
    def __init__(self, language):
        self.language = language


    def parse(self,datatype,document):
        print(self.language)
        lexer = get_lexer_by_name(self.language, stripall=True)
        formatter = HtmlFormatter(full="true")

        if datatype =='file':
            f = open(document,'r')
            c = f.read()
            op = highlight(c,lexer,formatter)
            f.close()
        else:
            op = highlight(document,lexer,formatter)

        return ({'lexerOp' :  op})

