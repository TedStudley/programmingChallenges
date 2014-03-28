# Project Euler Problem 001:
#
# 

module ProblemOne where

main = putStrLn $ show $ problemOne

problemOne :: Int
problemOne = foldl (+) 0 $ filter (\x -> x `mod` 3 == 0 || x `mod` 5 == 0) [1..999]
