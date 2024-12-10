from sly import Lexer
from sly.lex import LexError
#import operator

class SimpleLexer(Lexer):
    # token types :
    tokens = {IDENT, OP2, ENTIER}
    # token specifications :
    
    
    OP2 =    '[-+*/]'
    _entier_base_10= '[1-9](_?[0-9])*'
    _entier_base_8= '(0o|0O)[0-7](_?[0-7])*'
    _entier_base_16='(0o|0O)[0-9a-fA-F](_?[0-9a-fA-F])*'
    ENTIER = rf'{_entier_base_8}|{_entier_base_10}|{_entier_base_16}'
    IDENT =  '[A-Za-z][A-Za-z0-9]*'


    def ENTIER(self,t) :
        if self== _entier_base_10:
            t.value = int(t.value)
        elif self== _entier_base_8:
            t.value =str(value,2)+str(value,2,len(t.value-1))
        else:
            t.value = int(t.value[2:],16)
        return t
    
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value) 
        ignore_space= r'[ \t]+'
        
    @_(r'#.+$')
    def ignore_commentaire1(self,t):
        a=1
    @_(r'{[^{]+}')
    def ignore_commentaire2(self,t):
        a=1   
    @_(r'<!-[^<!-]+->')
    def ignore_commentaire3(self,t):
        a=1 
    
    def OP1(self,t):
        t.value=-t.value

    def OP2(self,t):
        if (t.value=='+' or t.value=='add'):
            return operateur.add
        elif t.value== '-' or t.value=='sub':
            return operateur.sub 
        elif t.value=='*' or t.value=='mul':
            return operateur.mul
        elif t.value=='/' or t.value=='div':
            return operateur.floordiv

if __name__ == '__main__':
    
    analyseur = SimpleLexer()
    #source = 'alpha+321*x5'
    print('entrez un texte à analyser');
    source = input()
    tokenIterator = analyseur.tokenize(source)
    try :
        for tok in tokenIterator :
            print(f'token -> type: {tok.type}, valeur: {tok.value} ({type(tok.value)}), ligne : {tok.lineno}')
    except LexError as erreur :
        print("Erreur à l'anayse lexicale ", erreur)
        
    

