#!/usr/bin/env python2

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
      return [[n]]
    elif n == 0:
      return [[0] * (x+1)]
    else:
      return [[i]+xs for i in xrange(n+1) for xs in dsets_(x-1,n-i)]

  return dsets_(9,n)

def to_digits(n,length=-1):
  ds = map(int,str(n))
  if length == -1:
    return ds
  else:
   return ([0] * (length - len(ds))) + ds

