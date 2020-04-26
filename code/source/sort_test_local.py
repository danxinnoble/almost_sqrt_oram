
import sys
import os
sys.path.append(os.path.abspath("/root/SCALE-MAMBA/Programs/shuffle"))

from shuffle_lib import waksman_io

from sys import argv

playerId = int(argv[1])
fout = open('Data/Player' + str(playerId) + '_in.txt', 'w')
fin = open('Data/Player' + str(playerId) + '_out.txt', 'r')

while True:
  line = fin.readline()
  command=int(line)

  if command==25:
    waksman_io(fin, fout)



