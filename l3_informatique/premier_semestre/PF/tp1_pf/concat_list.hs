liste2somme [(x:xs) , [] ] = [(x:xs)]
liste2somme [[] , y] = [y]
liste2somme [(x:xs) , y] = [x : liste2somme xs y]

