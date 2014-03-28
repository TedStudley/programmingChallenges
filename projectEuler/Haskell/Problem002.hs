module ProblemTwo where

main = putStrLn $ show $ problemTwo

problemTwo :: Integer
problemTwo = foldl (+) 0 $ takeWhile (\x -> x < 4000000) $ filter (\x -> x `mod` 2 == 0) $ fibs

fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
