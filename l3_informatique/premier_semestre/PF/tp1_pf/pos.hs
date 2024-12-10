myIndex :: [a] -> Int -> a 
myIndex(x:xs) pos = if pos==0 then x else myIndex xs (pos - 1)