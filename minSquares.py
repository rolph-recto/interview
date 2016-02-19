def getMinSquares(n):
	table = [(0, []) for i in xrange(n)]
	table[0] = (0, [])
	table[1] = (1, [1])
	table[2] = (2, [1,1])
	table[3] = (3, [1,1,1])

	for i in xrange(4,n):
		num = i + 1
		high = round(sqrt(num))
		possible = []
		for j in xrange(1, high+1):
			d = num / j
			possible += [ (h+table[num-(j*j*h)][0], table[num-(j*j*h)][1] + ([j] * d)) for h in xrange(1,d+1) ]
      
		table[i] = min(possible, lambda (x,y): x)

	return table[n-1][1]
    	
    	
  
  	

