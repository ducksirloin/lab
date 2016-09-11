fname1 = "strfile_Ac.txt"
f = open(fname1,"w")
a = -180
f.write("source leaprc.gaff\n")
for i in range(0,361):
	f.write("str" + str(i) + " = loadmol2 ACE.mol2\n")
	f.write("check str" + str(i) + "\n")
	f.write("mods = loadAmberParams ACE.frcmod\n")
	f.write("impose str" + str(i) + " {1} {{OD1 CG OD2 HD2 " + str(a+i) + "}}" + "\n")
	f.write("saveAmberParm str" + str(i) + "  confamb_Ac.prmtop confamb_Ac" + str(i) + ".inpcrd" + "\n")
f.close()

fname2 = "groupfile_Ac.sh"
f = open(fname2,"w")
f.write("#!/bin/sh"+ "\n")
for i in range(0,361):
	f.write("sander -O -i ener.in -c confamb_Ac" + str(i) + ".inpcrd -p confamb_Ac.prmtop -o dih_ener_Ac" + str(i) + ".out -r dih_ener_Ac"+ str(i) + ".restrt -x dih_ener_Ac"+ str(i) + ".mdcrd" + "\n")
f.close()

fname3 = "grep_Ac.sh"
f = open(fname3,"w")
f.write("#!/bin/sh"+ "\n")
f.write("grep -A4 -m1 NSTEP dih_ener_Ac0.out > allout_Ac.txt" + "\n")
for i in range(1,361):
	f.write("grep -A4 -m1 NSTEP dih_ener_Ac" + str(i) + ".out >> allout_Ac.txt" + "\n")
f.close()

fname4 = "grep_Ac_Gau.sh"
f = open(fname4, "w")
f.write("#!/bin/sh\n")
f.write("grep nuclear AcOH_dih.out > AcOH_nuclear.txt\n")
f.write("grep \"SCF Done\" AcOH_dih.out > AcOH_SCF.txt\n")
f.close()
