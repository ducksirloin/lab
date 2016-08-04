fname1 = "strfile.txt"
f = open(fname1,"w")
a = -180
for i in range(0,361):
	f.write("str" + str(i) + " = sequence{ACE GLH NME}" + "\n")
	f.write("impose str" + str(i) + " {2} {{OE1 CD OE2 HE2 " + str(a+i) + "}}" + "\n")
	f.write("savepdb str" + str(i) + "  GLH" + str(i) + ".pdb" + "\n")
f.close()

fname2 = "GLUP.sh"
f = open(fname2,"w")
f.write("#!/bin/sh"+ "\n")
for i in range(0,361):
	f.write("sed -i -e \"s/GLH /GLUP/g\" -e \"s/NME/NMA/g\" -e \"s/HB2/HB1/g\" -e \"s/HB3/HB2/g\" -e \"s/HG2/HG1/g\" -e \"s/HG3/HG2/g\" GLH" + str(i) +".pdb" + "\n")
f.close()

fname3 = "cmd_make_tpr_sh"
f = open(fname3,"w")
for i in range(361):
	f.write("/home/biostr1/tnagai/programs/gromacs-4.6.1-d-mpi-deb/bin/grompp_mpi_d -f seed.mdp -c charmm" + str(i) + ".gro -p charmm"+ str(i) +".top -o charmm"+ str(i) +".tpr -po mdout"+ str(i) +".mdp> logtpr"+ str(i) +".log\n")
f.close()

fname4 = "cmd_make_top_sh"
f = open(fname4, "w")
for i in range(361):
	f.write("~/tnagai/programs/gromacs-4.6.1-d-mpi-deb/bin/pdb2gmx_mpi_d -f GLH" + str(i) + ".pdb -o charmm" + str(i) + ".gro -p charmm" + str(i) + ".top -i posre" + str(i) + ".itp -ter <<EOF\n")
	f.write("1\n6\n3\n4\nEOF\n\n")
f.close()

fname5 = "do_sim_sh.csh"
f = open(fname5,"w")
for i in range(361):
	f.write("~/tnagai/programs/gromacs-4.6.1-d-mpi-deb/bin/mdrun_mpi_d  -s  charmm" + str(i) + ".tpr -e ener" + str(i) + ".edr -o traj" + str(i) + ".trr -x traj" + str(i) + ".xtc -cpo state" + str(i) + ".cpt -g md" + str(i) + ".log -c confout" + str(i) + ".gro > logmd" + str(i) + ".log\n")
f.close()

fname6 = "do_ener_sh.csh"
f = open(fname6,"w")
for i in range(361):
	f.write("~/tnagai/programs/gromacs-4.6.1-d/bin/g_energy_d -f  ener" + str(i) + ".edr  -s charmm" + str(i) + ".tpr -o ener" + str(i) + ".out -xvg none > log.ener <<EOF\n")
	f.write("3 4 6 9 14 15 16 0\n")
	f.write("EOF\n\n")
f.write("End your selection with an empty line or a zero.\n-------------------------------------------------------------------\n")
f.write("  1  Bond             2  U-B              3  Proper-Dih.      4  Improper-Dih. \n  5  CMAP-Dih.                            6  GB-Polarization                   \n")
f.write("  7  Nonpolar-Sol.    8  LJ-14            9  Coulomb-14      10  LJ-(SR)       \n 11  LJ-(LR)         12  Coulomb-(SR)    13  Coulomb-(LR)    14  Potential     \n")
f.write(" 15  Kinetic-En.     16  Total-Energy    17  Conserved-En.   18  Temperature   \n 19  Pressure        20  Constr.-rmsd    21  Vir-XX          22  Vir-XY        \n")
f.write(" 23  Vir-XZ          24  Vir-YX          25  Vir-YY          26  Vir-YZ        \n 27  Vir-ZX          28  Vir-ZY          29  Vir-ZZ          30  Pres-XX       \n")
f.write(" 31  Pres-XY         32  Pres-XZ         33  Pres-YX         34  Pres-YY       \n 35  Pres-YZ         36  Pres-ZX         37  Pres-ZY         38  Pres-ZZ       \n 39  #Surf*SurfTen   40  T-Protein \n")
f.close()
