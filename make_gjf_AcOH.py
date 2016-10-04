# -*- coding: utf-8 -*-
fname1 = "AcOH_dih_ff14ipq.gjf"
f = open(fname1,"w")
f.write("%mem=130MW\n")
f.write("%Chk=C:\Doccuments and Settings\デスクトップ\n")
for i in range(37):
    fname = "confamb_Ac" + str(i * 10) + ".inpcrd"
    n = 0
    f.write("#T MP2/cc-pVTZ Test\n\nCOOH\n\n0 1\n")
    for f1 in open(fname,"r"):
        x = f1.split()
        if n == 2:
            f.write("C1     "+str(x[0])+" "+str(x[1])+" "+str(x[2])+"  \n")
            f.write("O1     "+str(x[3])+" "+str(x[4])+" "+str(x[5])+"  \n")
        elif n == 3:
            f.write("O2     "+str(x[0])+" "+str(x[1])+" "+str(x[2])+"  \n")
            f.write("H1     "+str(x[3])+" "+str(x[4])+" "+str(x[5])+"  \n")
        elif n == 4:
            f.write("C2     "+str(x[0])+" "+str(x[1])+" "+str(x[2])+"  \n")
            f.write("H2     "+str(x[3])+" "+str(x[4])+" "+str(x[5])+"  \n")
        elif n == 5:
            f.write("H3     "+str(x[0])+" "+str(x[1])+" "+str(x[2])+"  \n")
            f.write("H4     "+str(x[3])+" "+str(x[4])+" "+str(x[5])+"  \n\n")
        if n == 5 and i < 36:
            f.write("--Link1--\n")
        n += 1
f.close()
