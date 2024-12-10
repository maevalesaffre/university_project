_entier_base_10= '[1-9](_?[0-9])*'
_entier_base_8= '(0o|0O)[0-7](_?[0-7])*'
_entier_base_16='(0o|0O)[0-9a-fA-F](_?[0-9a-fA-F])*'
OP2= '[-+*/]|(add|ADD)|(sub|SUB)|(mul|MUL)|(floordiv|FLOORDIV)'
OP1= 'opp|OPP'
SET= '->[A-Za-z][A-Za-z0-9]*'
ENTIER= '[0-9]+|(Oo|OO)[0-7]+([]?[0-7])*|(Ox|OX)[0-9a-fA-F]+([]?[0-9a-fA-F])*'
IDENT='[A-Za-z[A-Za-z0-9]*'
POP='pop|POP'

def OP1(self,t):
    t.value= lambda x:-x
    return t

def set(self,t):
    l=list(t.value)
    l.pop(0)
    l.pop(0)
    t.value="".join(elt for elt in l)
    return t

def POP(self,t):
    if t.value=='pop' or t.value='POP':
        return t

def Entier(self,t):
    if (t.value[0:2]=='Oo')or(t.value[0:2]=='OO'):
        t.value=int(t.value[2:],8)
    elif (t.value[0:2]=='Ox')or(t.value[0:2]=='OX'):
        t.value=int(t.value[2:],16)
    else:
        t.value=int(t.value)
    return t