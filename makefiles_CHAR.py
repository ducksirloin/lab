fname1 = "strfile.txt"
f = open(fname1,"w")
a = -180
for i in range(0,361):
	f.write("set default PBradii mbondi2" + "\n")
	f.write("str" + str(i) + " = sequence{ACE GLH NME}" + "\n")
	f.write("impose str" + str(i) + " {2} {{OE1 CD OE2 HE2 " + str(a+i) + "}}" + "\n")
	f.write("savepdb str" + str(i) + "  GLH" + str(i) + ".pdb" + "\n")
f.close()

fname2 = "GLUP.sh"
f = open(fname2,"w")
f.write("#!/bin/sh"+ "\n")
for i in range(0,361):
	f.write("sed -i -e \"s/GLH /GLUP/g\" -e \"s/NME/NMA/g\" GLH" + str(i) +".pdb" + "\n")
f.close()

fname3 = "cmd_make_tpr_sh"
f = open(fname3,"w")
for i in range(361):
	f.write("/home/biostr1/tnagai/programs/gromacs-4.6.1-d-mpi-deb/bin/grompp_mpi_d -f seed.mdp -c charmm" + str(i) + ".gro -p charmm"+ str(i) +".top -o charmm"+ str(i) +".tpr > logtpr"+ str(i) +".log\n")
f.close()
