sommeDeXaY x y = if x > y then 0 else x + sommeDeXaY (x+1) y

--sommeDeXaY x y |x > y = 0  
--	       |x + sommeDeXaY (x+1) y
