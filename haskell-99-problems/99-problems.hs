--Problem 3: Find the K'th element of a list. The first 
--	     element in the list is number 1.
elementAt (x:xs) y
  | x == y = y
  | x /= y = elementAt xs y


--Problem 2: Find the last but one element of a list
myButLast [x,y] = x
myButLast (h:b) = myButLast b

--Problem 1: Find the last element of a list
myLast [x] = x
myLast (h:b) = myLast b
