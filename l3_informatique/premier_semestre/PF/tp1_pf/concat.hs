plusplus (x:xs) [] = (x:xs)
plusplus [] y = y
plusplus (x:xs) y = x : plusplus xs y

liste2somme [(x:xs) , [] ] = [(x:xs)]
liste2somme [[] , y] = [y]
liste2somme [(x:xs) , y] = [x : plusplus xs y]


map1 _ [] = []
map1 f (x:xs) = f x : map1 f xs


