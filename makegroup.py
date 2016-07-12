fname = "groupfile.txt"
f = open(fname,"w")
f.write("#The group file for 360 pattern MD"+ "\n")
for i in range(0,361):
	f.write("-O -i mdin.ener -c confamb" + str(i) + ".inpcrd -p confamb" + str(i) + ".prmtop -o dih_ener" + str(i) + ".out -r dih_ener"+ str(i) + ".restrt -x dih_ener"+ str(i) + ".mdcrd" + "\n")
