import numpy as np

def waksman_id():
  return 25

def waksman_io(fin, fout):
  
  line = fin.readline()
  logArraySize = int(line)  

  arraySize = 2**logArraySize

  p = np.random.permutation(arraySize)
  gates = createGates(p)
  for i in range(len(gates[0])):
    for j in range(len(gates)):
      fout.write(str(gates[j][i]) + "\n")

  fout.flush()


def swapParity(x):
  if x%2 == 0:
    y = x + 1
  else:
    y = x - 1
  return y

# Where p is a permutation
def createGates(p): 
  n = p.size
  logN = int(np.log2(n))
  halfN = int(n/2)
 
  gates = np.ndarray(shape=(halfN, 2*logN - 1), dtype = int)

  if p.size == 2:
    # i.e. if permutation is [0, 1] (identity) gate should be identity
    gates[0][0] = p[0] 
    return gates  

  invP = np.empty_like(p)
  invP[p] = np.arange(p.size)

  # Figure out which elems should go in which sub-permutations
  top = np.empty(halfN, dtype = int)
  bot = np.empty_like(top)

  unallocated = set(p)

  i = 0
  while i < halfN:
    a = unallocated.pop()
    unallocated.add(a)
    while a in unallocated:
      # a and b will use the same input switch
      #   so will need to be in different sub-permutation blocks
      unallocated.remove(a)
      top[i] = a
      b = swapParity(a)    
      bot[i] = b
      unallocated.remove(b)

      # nextA chosen such that it needs to be in a different block as b
      # Therefore nextA will be in the same block as a (namely top block).
      pB = p[b]
      pNextA = swapParity(pB)
      nextA = invP[pNextA]
      a = nextA
      i = i + 1

  gatesIn = np.empty(halfN)
  gatesOut = np.empty_like(gatesIn)

  topIns = top.copy()
  topIns.sort()
  topOutDest = np.empty_like(top)

  for i in range(halfN):
    gatesIn[i] = topIns[i] % 2
    topOutDest[i] = p[top[i]]
  
  topOutDest.sort()
  for i in range(halfN):
    gatesOut[i] = topOutDest[i] % 2

  # For every pair (2d, 2d+1), pTop cantains one, pBot the other
  # Similarly, p(pTop) will contain one, p(pBot) the other.
  # Therefore given i -> p(i) with i in top,
  #   we can add floor(i/2) -> floor(p(i)/2) to pTop.
  pTop = np.empty_like(top)
  pBot = np.empty_like(bot)
  for i in range(halfN):
    pTop[int(top[i]/2)] = int(p[top[i]]/2)
    pBot[int(bot[i]/2)] = int(p[bot[i]]/2)

  gatesTop = createGates(pTop)
  gatesBot = createGates(pBot)

  for i in range(halfN):
    gates[i][0] = gatesIn[i]
    gates[i][2*logN-2] = gatesOut[i]
      

  for i in range(int(halfN/2)):
    for j in range(1, 2*logN - 2):
      gates[i][j] = gatesTop[i][j-1]
      gates[i+ int(halfN/2)][j] = gatesBot[i][j-1]

  return gates
  

  
