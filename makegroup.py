fname = "groupfile.sh"
f = open(fname,"w")
f.write("#!/bin/sh"+ "\n")
for i in range(0,361):
	f.write("sander -O -i ener.in -c confamb" + str(i) + ".inpcrd -p confamb" + str(i) + ".prmtop -o dih_ener" + str(i) + ".out -r dih_ener"+ str(i) + ".restrt -x dih_ener"+ str(i) + ".mdcrd" + "\n")
