dset n = dset' 9 n
  where dset' 0 n = [[n]]
        dset' x 0 = [take (x+1) $ repeat 0]
        dset' x n = do
          i <- [0..n]
          xs <- dset' (x-1) (n-i)
          return (i:xs)
      
