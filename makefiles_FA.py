fname1 = "strfile_FA.txt"
f = open(fname1,"w")
a = -180
for i in range(0,361):
	f.write("source leaprc.gaff\n")
	f.write("str" + str(i) + " = loadmol2 HCOOH.mol2\n")
	f.write("check str" + str(i) + "\n")
	f.write("mods = loadAmberParams HCOOH.frcmod\n")
	f.write("impose str" + str(i) + " {1} {{OD1 CG OD2 HD2 " + str(a+i) + "}}" + "\n")
	f.write("saveAmberParm str" + str(i) + "  confamb_FA.prmtop confamb_FA" + str(i) + ".inpcrd" + "\n")
f.close()

fname2 = "groupfile_FA.sh"
f = open(fname2,"w")
f.write("#!/bin/sh"+ "\n")
for i in range(0,361):
	f.write("sander -O -i ener.in -c confamb_FA" + str(i) + ".inpcrd -p confamb_FA.prmtop -o dih_ener_FA" + str(i) + ".out -r dih_ener_FA"+ str(i) + ".restrt -x dih_ener_FA"+ str(i) + ".mdcrd" + "\n")
f.close()

fname3 = "grep_FA.sh"
f = open(fname3,"w")
f.write("#!/bin/sh"+ "\n")
f.write("grep -A4 -m1 NSTEP dih_ener_FA0.out > allout_FA.txt" + "\n")
for i in range(1,361):
	f.write("grep -A4 -m1 NSTEP dih_ener_FA" + str(i) + ".out >> allout_FA.txt" + "\n")
f.close()

fname4 = "grep_FA_Gau.sh"
f = open(fname4, "w")
f.write("#!/bin/sh\n")
f.write("grep nuclear FA_dih.out > FA_nuclear.txt\n")
f.write("grep \"SCF Done\" FA_dih.out > FA_SCF.txt\n")
f.close()
