import psycopg2 as db_api

att_names = lambda cur : (att[0] for att in cur.description)
row_dict = lambda cur,row : dict(zip(att_names(cur),row))


class DataLayer :
    def __init__(self, **connection_parms) :
        self.conn=db_api.connect(**connection_parms)
        self.conn.autocommit=True
        self.conn.cursor().execute('set search_path = course')
        
    def equipes(self) :
        """
            Renvoie la liste des noms d'étapes
        """
        cur = self.conn.cursor()
        cur.execute('select * from equipes')
        return cur.fetchall()

    def liste_noms_etapes(self) :
        """
            Renvoie la liste des noms d'étapes
        """
        cur = self.conn.cursor()
        cur.execute('''
            select nom
            from etapes
            order by numero
        ''')
        res = []
        for row in cur :
            res.append(row[0])
        return res
    
    def coureur_par_nom(self, nom) :
        """
            Recherche un coureur de ce nom
            Renvoie un tuple (dossard, nom de coureur, nom d'équipe, taille)
            ou None si le coureur n'existe pas
        """
        cur = self.conn.cursor()
        ## NE PAS FAIRE :
        #cur.execute("select * from coureurs where coureurs.nom = '%(var)s' "%{'var':nom})
        ## NE PAS FAIRE :
        #cur.execute("select * from coureurs where coureurs.nom = '"+ nom + "'")
        
        # mais faire :
        cur.execute("select * from coureurs where coureurs.nom = %(var)s ", {'var':nom})
        #print(cur.query)
        return cur.fetchone()
    
    def coureurs(self) :
        """
            Renvoie la liste des coureurs engagés :
            une liste de tuples (dossard, nom de coureur, nom d'équipe, couleur du maillot, taille)
            classée par dossard
        """
        pass # en attendant...
         
         
        
            
    def set_chrono(self, coureur, etape, mesure) :
        """
            Enregistre un chrono dans la table temps
            
            param coureur : numéro de dossard
            param etape : numéro d'étape
            param mesure : temps sous forme de chaîne de caractère
        """
        pass # en attendant...

    def classement_etape(self, num_etape) :
        """
            renvoie le tableau de classement à l'étape num_etape
            
            tableau de tuples (dossard, nom du coureur, nom de l'equipe, chrono, rang)
            par ordre d'arrivée à l'étape
        """
        pass # en attendant...
       
    def chronos(self, coureur) :
        """
            renvoie la table des chronos d'un coureur
            
            tableau de tuples (numero étape, nom étape, chrono du coureur)
            (le dernier attribut peut être None)
            par ordre de numéro  d'étapes
        """
        pass # en attendant...
       
        