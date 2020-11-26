-- hell_world = "Hello World"
-- numbers = [1..10]

-- -- printNumbers x = print (show x)
-- -- fc = map printNumbers numbers
-- printLst :: [Int] -> String
-- printLst [] = ""
-- printLst [x] = (show x)
-- printLst (x:xs) = (show x) ++ " " ++ printLst xs

-- main :: IO()
-- main = mapM_ putStrLn $ map print [1..8]
-- --     map printNumbers numbers
-- -- main = print (hell_world)
-- -- main = putStrLn hell_world

-- printItem [] = return ()
printItem (x:xs) = putStrLn x >> printItem xs

fizzBuzz :: Int -> String
fizzBuzz n | n `mod` 15 == 0  = "FizzBuzz"
       | n `mod` 3  == 0  = "Fizz"
       | n `mod` 5  == 0  = "Buzz"
       | otherwise        = show n

main :: IO()
main = printItem $ map fizzBuzz [1..100]