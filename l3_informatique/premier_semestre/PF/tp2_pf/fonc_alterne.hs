-- alterne

alterne [] = []
alterne (x:xs) = x : alterne(drop 1 xs)

-- combine
combine :: (a -> b -> c) -> [a] -> [b] -> [c]
combine f _ [] = []
combine f [] _ = []
combine f (x:xs) (y:ys) = (f x y) : combine f xs ys 


-- pascal