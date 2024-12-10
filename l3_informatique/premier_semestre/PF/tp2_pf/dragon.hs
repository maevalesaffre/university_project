module Main where

import Graphics.Gloss

alterne :: [a] -> [a]

alterne [] = []
alterne [x] = [x]
alterne (x:_:zs) = x : alterne zs

combine :: (a -> b -> c) -> [a] -> [b] -> [c]
combine _ _  [] = []
combine _ [] _  = []
combine f (x:xs) (y:ys) = f x y : combine f xs ys 

pasPascal :: [Integer] -> [Integer]
pasPascal xs = zipWith (+) (xs++[0])  (0:xs)

pascal :: [[Integer]]
pascal = iterate pasPascal [1]

pointAintercaler :: Point -> Point -> Point 
pointAintercaler (x,y) (x1,y1) = ((x+x1)/2 + (y1-y)/2,(y+y1)/2 + (x-x1)/2)

pasDragon :: Path -> Path 
pasDragon [] = []
pasDragon [a] = [a]
pasDragon [a,b] = [a,pointAintercaler a b,b]
pasDragon (a:b:c:xs) = a : pointAintercaler a b : b : pointAintercaler c b : pasDragon (c:xs)



main :: IO()
main = animate (InWindow "Dragon" (500, 500) (0, 0)) white (dragonAnime (50,250) (450,250))

dragonAnime :: Point -> Point -> Float -> Picture
dragonAnime a b t = Line (dragon a b !! (round t `mod` 20))

dragon :: Point -> Point -> [Path]
dragon a b = iterate pasDragon [a,b]
 


