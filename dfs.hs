import System.Environment
import System.IO
import Data.List

dfs :: Eq a => Monad m => (a -> m b) -> [(a,a)] -> a -> m [b]
dfs visit g head = dfs' visit g [] [head]
  where dfs' visit g visited [] = return []
        dfs' visit g visited (v:vs) = do
          let children = filter (not . (`elem` visited)) $ map snd $ filter ((== v) . fst) g
          r <- visit v
          rs <- dfs' visit g (v:visited) (children ++ vs)
          return (r:rs)

main = do
  fname:_ <- getArgs
  withFile fname ReadMode $ \h -> do
    fstr <- hGetContents h
    let flines = lines fstr
    let g = map (\(a,b) -> (fst a, fst b)) $ uncurry zip $ partition ((== 0) . snd) $ zip flines $ cycle [0,1] 
    dfs putStrLn g "1"
    return ()
