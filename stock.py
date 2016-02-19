#!/usr/bin/env python
def getMaxStock(A):
  lo = 0
  hi = 0
  new_lo = 0
  new_hi = 0
  for i in xrange(1,len(A)):
    # must move new_hi also because it can't be before new_lo
    # i.e., you must buy low first to sell high
    if A[i] < A[new_lo]:
      new_lo = i
      new_hi = i
      
    elif A[i] > A[new_hi]:
      new_hi = i

    if A[new_hi] - A[new_lo] > A[hi] - A[lo]:
      lo = new_lo
      hi = new_hi

  return lo, hi

def main():
  stock = [44, 45, 30, 100]
  lo, hi = getMaxStock(stock)
  print "Buy on day {}, sell on day {} for profit of {}".format(lo+1, hi+1, stock[hi]-stock[lo])

  stock2 = [47.0, 44.0, 45.0, 46.0, 42.0, 43.0]
  lo2, hi2 = getMaxStock(stock2)
  print "Buy on day {}, sell on day {} for profit of {}".format(lo2+1, hi2+1, stock2[hi2]-stock2[lo2])
  
if __name__ == "__main__":
  main()
