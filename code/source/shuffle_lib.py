
def waksman_id():
  return 25

def waksman_io(fin, fout):
  
  line = fin.readline()
  logArraySize = int(line)  

  arraySize = 2**logArraySize

  # Hard-coded gates. This is obviously insecure. 
  # Will replace with actual gates.
  nGates = int((logArraySize * 2 - 1) * arraySize / 2)
  for i in range(nGates):
    fout.write(str(1) + "\n")

  fout.flush()
