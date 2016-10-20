fname1 = "ambpdb.sh"
f = open(fname2, "w")
for i in range(361):
    f.write("ambpdb -p confamb.prmtop < confamb" + str(i) + ".inpcrd > ACE" + str(i) + ".pdb\n")


fname2 = "RISM_do.sh"
f = open(fname2, "w")
for i in range(361):
    f.write("sander -O -i ener.in -c confamb" + str(i) + ".inpcrd -p confamb.prmtop ")
    f.write("-o rism_do" + str(i) + ".out -r rism_do" + str(i) + ".restrt -x rism_do" + str(i) + ".mdcrd ")
    f.write("-xvv ../3-Solvent/SPC_NaCl" + str(i) + ".xvv -guv guvroot -huv huvroot -cuv cuvroot ")
    f.write("-uuv uuvroot -asymp asympfile -quv quvroot -chgdist chgdistroot\n")
