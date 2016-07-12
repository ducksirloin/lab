fname = "grep.sh"
f = open(fname,"w")
f.write("#!/bin/sh"+ "\n")
for i in range(0,361):
	f.write("grep -A4 -m1 NSTEP dih_ener" + str(i) + ".out >> allout.txt" + "\n")
