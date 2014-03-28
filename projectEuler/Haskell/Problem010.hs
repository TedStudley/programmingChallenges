module ProblemTen where

main = putStrLn $ show $ problemTen

problemTen :: Integer
problemTen = foldr (+) 0 $ takeWhile (\x -> x < 2000000) primes

primes :: [Integer]
primes = 2 : 3 : ([5,7..] `minus` unionAll [[p*p, p*p+2*p..] | p <- tail primes])
  where 
    unionAll = foldr (\(x:xs)->(x:).union xs) []
    minus (x:xs) (y:ys) = case (compare x y) of
                LT -> x : minus    xs  (y:ys)
                EQ ->     minus    xs     ys
                GT ->     minus (x:xs)    ys
    minus    xs   _     = xs
    union (x:xs) (y:ys) = case (compare x y) of
                LT -> x : union    xs  (y:ys)
                EQ -> x : union    xs     ys
                GT -> y : union (x:xs)    ys
    union    xs     []  = xs
    union    []     ys  = ys
