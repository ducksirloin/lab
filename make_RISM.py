fname1 = "ambpdb.sh"
f = open(fname2, "w")
for i in range(361):
    f.write("ambpdb -p confamb.prmtop < confamb" + str(i) + ".inpcrd > ACE" + str(i) + ".pdb\n")
f.close()

fname2 = "RISM_do.sh"
f = open(fname2, "w")
for i in range(361):
    f.write("sander -O -i ener.in -c confamb" + str(i) + ".inpcrd -p confamb.prmtop ")
    f.write("-o rism_do" + str(i) + ".out -r rism_do" + str(i) + ".restrt -x rism_do" + str(i) + ".mdcrd ")
    f.write("-xvv SPC_NaCl.xvv -guv guvroot -huv huvroot -cuv cuvroot ")
    f.write("-uuv uuvroot -asymp asympfile -quv quvroot -chgdist chgdistroot\n")
f.close()

fname3 = "grep_RISM.sh"
f = open(fname3, "r")
f.write("grep -A4 -m1 NSTEP rism_do0.out > RISM_result.txt\n")
for i in range(1, 361):
    f.write("grep -A4 -m1 NSTEP rism_do" + str(i) + ".out >> RISM_result.txt\n")
f.close()
