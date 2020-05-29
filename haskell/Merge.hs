merge :: (Ord a) => [a] -> [a] -> [a]
merge xs [] = xs
merge [] ys = ys
merge left@(l:ls) right@(r:rs) = if l <= r
                                    then l : merge ls right
                                    else r : merge left rs

main = print $ merge [1, 3, 5] [2, 4, 6]
