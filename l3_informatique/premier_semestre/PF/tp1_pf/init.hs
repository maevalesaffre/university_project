myInit :: [a] -> [a] 
myInit xs = take taille xs
    where taille = length xs -1
