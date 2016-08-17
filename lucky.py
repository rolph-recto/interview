#!/usr/bin/env python2

import sys

def is_prime(num):
  # prime numbers are greater than 1
  if num > 1:
    # check for factors
    for i in range(2,num):
      if (num % i) == 0: return False

    return True

  else:
    return False

def is_lucky(dset):
  return is_prime(sum([i*dset[i] for i in xrange(10)])) \
    and is_prime(sum([(i**2)*dset[i] for i in xrange(10)]))

def dsets(n):
  def dsets_(x,n):
    if x == 0:
      yield [n]
    elif n == 0:
      yield [0] * (x+1)
    else:
      for i in xrange(n+1):
        for xs in dsets_(x-1, n-i):
          yield [i]+xs

  return dsets_(9,n)

def to_digits(n,length=-1):
  ds = map(int,str(n))
  if length == -1:
    return ds
  else:
   return ([0] * (length - len(ds))) + ds

fac_mem = {}
def fac(n):
  global fac_mem
  if n in fac_mem:
    return fac_mem[n]
  else:
    res = n*fac(n-1)
    fac_mem[n] = res
    return res

def count_dset_lucky(dset, lo, hi):
  def count_dset_lucky_(dset, l, i, dlo, dhi):
    if i >= l:
      return 1
    else:
      paths = 0

      # fix a digit, and then recurse down
      for x in xrange(dlo[i], dhi[i]+1):
        # digit 
        if dset[x] > 0:
          dset2 = dset[:]
          dset2[x] -= 1
          # short circuit digits "in the middle"
          # by counting them as (n-1)!, where n is the
          # number of remaining digits left
          if x > dlo[i] and x < dhi[i]:
            print "digifac", dset
            print "infofac", dset2, l, i+1, dlo, dhi
            paths += fac(sum(dset2))
          else:
            print "digirec", dset
            print "inforec", dset2, l, i+1, dlo, dhi
            paths += count_dset_lucky_(dset2, l, i+1, dlo, dhi)

      return paths

  length = sum(dset)
  return count_dset_lucky_(dset, length, 0, to_digits(lo, length), to_digits(hi, length))
  
def main():
  lo, hi = int(sys.argv[1]), int(sys.argv[2])
  paths = 0
  length = len(to_digits(hi))
  for dset in dsets(length):
    if is_lucky(dset):
      print "lucky", dset
      paths += count_dset_lucky(dset, lo, hi)

  print paths

if __name__ == "__main__":
  main()
