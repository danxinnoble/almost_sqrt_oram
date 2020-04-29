for halfD in range(1, 7):
  n = 2**(2*halfD)
  m = int(n - n**(3/8))
  print("n=" + repr(n) + " m=" + repr(m))
