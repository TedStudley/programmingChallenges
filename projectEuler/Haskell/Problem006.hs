module ProblemSix where

main = putStrLn $ show $ problemSix

problemSix :: Integer
problemSix = squareOfSum - sumOfSquares
  where
    squareOfSum = (\x -> x * x) $ foldr (+) 0 [1..100]
    sumOfSquares = foldr (+) 0 [x*x | x <- [1..100]]
