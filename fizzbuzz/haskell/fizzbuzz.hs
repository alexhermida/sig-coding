printItem [] = return () -- match an empty list
printItem (x:xs) = putStrLn x >> printItem xs -- match a list with at least two elements

fizzBuzz :: Int -> String
fizzBuzz n | n `mod` 15 == 0  = "FizzBuzz"
       | n `mod` 3  == 0  = "Fizz"
       | n `mod` 5  == 0  = "Buzz"
       | otherwise        = show n

main :: IO()
main = printItem $ map fizzBuzz [1..100]