import Graphics.Gloss

type Symbole  = Char
type Mot      = [Symbole]
type Axiome   = Mot
type Regles   = Symbole -> Mot
type LSysteme = [Mot]
type EtatTortue = (Point, Float)
type EtatDessin = (EtatTortue, Path)
type Config = (EtatTortue -- Etat initial de la tortue
              ,Float      -- Longueur initiale d’un pas
              ,Float      -- Facteur d’echelle
              ,Float      -- Angle pour les rotations de la tortue
              ,[Symbole]) -- Liste des symboles compris par la tortue 




regle :: Symbole  -> Mot
regle 'F' = "F-F++F-F"
regle '+' = "+"
regle '-' = "-"
regle _ = ""

motSuivant :: Regles -> Mot -> Mot
motSuivant _ [] = []
motSuivant f (x:xs) = f x ++ motSuivant f xs


motSuivant' f xs = [c | x <- xs, c <- f x]

motSuivant'':: Regles -> Mot -> Mot
motSuivant'' = concatMap

lsysteme :: Axiome -> Regles -> LSysteme
lsysteme x r = iterate (motSuivant r) x 

etatInitial :: Config -> EtatTortue
etatInitial (x,y,z,z',z'') = x

longueurPas :: Config -> Float
longueurPas (x,y,z,z',z'') = y


facteurEchelle :: Config -> Float
facteurEchelle (x,y,z,z',z'') = z

angle :: Config -> Float
angle (x,y,z,z',z'') = z'

symbolesTortue :: Config -> [Symbole]
symbolesTortue (x,y,z,z',z'') = z''

avance :: Config -> EtatTortue -> EtatTortue
avance c ((x,y),p) = ((x+(longueurPas c)*cos(p),(longueurPas c)*sin(p)),p)

tourneAGauche :: Config -> EtatTortue -> EtatTortue
tourneAGauche c (p,f) = (p,f + (angle c))

tourneADroite :: Config -> EtatTortue -> EtatTortue
tourneADroite c (p,f) = (p,f - (angle c))

filtreSymbolesTortue :: Config -> Mot -> Mot
filtreSymbolesTortue tortue mots = filter (\x -> x `elem` (symbolesTortue tortue)) mots

interpreteSymbole :: Config -> EtatDessin -> Symbole -> EtatDessin
interpreteSymbole a b c 
    | b <= avance = avance a ((x,y),p)
    | b <= tourneAGauche = tourneAGauche a (p,f)
    | b <= tourneADroite = tourneADroite a (p,f)
    | otherwise   = "blbla"
