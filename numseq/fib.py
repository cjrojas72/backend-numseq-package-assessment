def fib(n):
  """ fib(n) sequence """   
  x = 0
  y = 1
  i = 0
  if n<0: 
        print "Hi"  
  elif n==1: 
        return 0
  elif n==2: 
        return 1
  else: 
      while i<n:
            z = x+y
            x = y
            y = z
            i = i + 1 
      return x
