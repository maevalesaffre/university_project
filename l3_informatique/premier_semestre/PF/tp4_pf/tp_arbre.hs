--import Test.QuickCheck

--Question1

data Arbre coul val = Feuille | Noeud coul val (Arbre coul val) (Arbre coul val) deriving (Show)    

monArbreComplet = Noeud 'a' 1 (Noeud 'b' 2 Feuille Feuille) (Noeud 'c' 3 Feuille Feuille)
monArbre = Noeud 'R' 1 (Noeud 'B' 2 (Noeud 'B' 4 Feuille Feuille) Feuille) (Noeud 'B' 3 (Noeud 'B' 5 Feuille Feuille) Feuille)                   
                      
--Question2

mapArbre :: (a -> b) -> Arbre coul a -> Arbre coul b
mapArbre _ Feuille = Feuille
mapArbre f (Noeud coul val gauche droite) = Noeud coul (f val) (mapArbre f gauche) (mapArbre f droite)

foldArbre :: (coul -> val -> b -> b -> b) -> b -> Arbre coul val -> b
foldArbre _ r Feuille = r
foldArbre f r (Noeud coul val gauche droite) =  f coul val (foldArbre f r gauche) (foldArbre f r droite)

--Question3  
  
--Hauteur recursive
hauteur1 :: Arbre coul val -> Int
hauteur1 Feuille = 0
hauteur1 (Noeud c v g d) = max (1 + hauteur1 g) (1 + hauteur1 d)

--Hauteur fold
hauteur2 :: Arbre coul val -> Int
hauteur2 a = foldArbre (\x y z t -> (max z t) + 1) 0 a

--Taille recursive
taille1 :: Arbre coul val -> Int
taille1 Feuille = 0
taille1 (Noeud c v g d) = 1 + hauteur1 g + hauteur1 d

--Taille fold
taille2 :: Arbre coul val -> Int
taille2 a = foldArbre (\x y z t -> z + t + 1) 0 a


--Question4
peigneGauche :: [(c,a)] -> Arbre c a
peigneGauche [] = Feuille
peigneGauche ((c,a):xs) = Noeud c a (peigneGauche xs) Feuille


--Question5
-- Elle verifie si la longueur de la liste passe en parametre est egale a la hauteur du peigneGauche de cette liste.

--Question6
--prop_hauteurPeigne xs = length xs == hauteur1 (peigneGauche xs)

--Question8
estParfait :: Arbre c a -> Bool
estParfait Feuille = True
estParfait (Noeud _ _ g d) = estParfait fg && estParfait fd && hauteur fg == hauteur fd

--Question9

--Question10
-- Les peignes gauches complets sont les peignes gauches de hauteur 1


--Question11
parfait :: Int ->[(c,a)] -> Arbre c a
parfait 0 _ = Feuille
parfait h xs = Noeud c v (parfait (h-1) xs) (parfait (h-1) (drop(n+1) xs))
                where (c,v) = xs!!n
                n = (2^(h-1)) - 1

--Question12
repeat' :: a -> [a]
repeat' = iterate id

--Question
infiniteList :: [Char] -> [((), Char)]
infiniteList (x:xs) = ((), x) : infiniteList xs

createInfinitList :: [((), Char)]
createInfinitList = infiniteList ['a'..]

--Question14
aplatit :: Arbre c a -> [(c, a)]
aplatit Feuille = []
aplatit (Noeud c v g d) = aplatit g ++ [(c,v)] ++ aplatit d

--Question15
element :: Eq a => a -> Arbre c a -> Bool
element el Feuille = False
element el (Noeud _ v g d) 
                        |el == v = True
                        |otherwise = (element el g) || (element el d)


--Question16
