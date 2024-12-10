# utilitaire affichage table sous forme de texte

def tuple_to_str (l, w=(6,), a=('<',)) :
    w += w[-1:]*(len(l)-len(w))
    a += a[-1:]*(len(l)-len(a))
    cells = ('{{:{}{}}}'.format(a[i],w[i]).format(str(l[i])[:w[i]]) for i in range(len(l)))
    return  f"|{'|'.join(cells)}|"

def table_to_str (tab) :
    """
        renvoie une chaîne avec le contenu de la table formaté en colonnes
    """
    if len(tab) == 0 :
        return '(vide)\n'
    largeurs_col = lambda i :(len(str(line[i])) for line in tab)
    w = [max(largeurs_col(col)) for col in range(len(tab[0]))]
    bord= '-' * (sum(w)+len(w)+1) +'\n'
    align = [ '>' if isinstance(x,int) else '<' for x in tab[0] ]
    buffer = [tuple_to_str(line, w, align) for line in tab]
    return bord + '\n'.join(buffer) +'\n'+ bord
