module ProblemNine where

main = putStrLn $ show problemNine

problemNine :: Integer
problemNine = (\(a,b,c) -> a*b*c) $ head $ filter (\(a,b,c) -> a+b+c == 1000) triples

triples :: [(Integer, Integer, Integer)] 
triples = filter (\(a,b,c) -> a*a + b*b == c*c) $ [(a,b,c) | c <- [0..], b <- [1..(c-1)], a <- [0..(b-1)]]
