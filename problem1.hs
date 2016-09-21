-- Problem 1: Find the last element of a list
import Control.Monad
import Data.Char

m :: String
m = "Input numbers: "

plus5 :: Int -> Int
plus5 x = x + 5

main :: IO ()
main = do
    putStrLn m
	n <- getLine
	let nu = read n :: Integer
    let num = plus5 nu
    print num
