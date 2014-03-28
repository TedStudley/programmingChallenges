module ProblemFour where

main = putStrLn $ show $ problemFour

problemFour :: Integer
problemFour = max $ palindromes
  where
    max (x:xs) = maxHelper x xs
      where
        maxHelper y (x:xs) = case (compare x y) of
          LT -> maxHelper y xs
          GT -> maxHelper x xs
          EQ -> maxHelper x xs
        maxHelper y []     = y

palindromes :: [Integer]
palindromes = filter (palindromeQ) $ [a*b | a <- [100..999], b <- [100..999]]
  where
    palindromeQ x = (\y -> y == reverse y) $ show x
