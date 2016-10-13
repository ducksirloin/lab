# -*- coding: utf-8 -*-
fname1 = "B3LYP_AUG_ff14SBstr_36.gjf"
f = open(fname1,"w")
f.write("%mem=130MW\n")
f.write("%Chk=C:\Doccuments and Settings\デスクトップ\n")
fname = "B3LYP_AUG_14SB_hyd.txt"
fname2 = "B3LYP_AUG_14SBstr.txt"
for f2 in open(fname2, "r"):
    x = f2.split()

n = 0
for f1 in open(fname,"r"):
    y = f1.split()
    f.write("#T B3LYP/AUG-cc-pVDZ Test\n\nCOOH\n\n0 1\n")
    f.write("C1     "+str(x[0])+" "+str(x[1])+" "+str(x[2])+"  \n")
    f.write("O1     "+str(x[3])+" "+str(x[4])+" "+str(x[5])+"  \n")
    f.write("O2     "+str(x[6])+" "+str(x[7])+" "+str(x[8])+"  \n")
    f.write("H1     "+str(x[9])+" "+str(y[0])+" "+str(y[1])+"  \n")
    f.write("C2     "+str(x[10])+" "+str(x[11])+" "+str(x[12])+"  \n")
    f.write("H2     "+str(x[13])+" "+str(x[14])+" "+str(x[15])+"  \n")
    f.write("H3     "+str(x[16])+" "+str(x[17])+" "+str(x[18])+"  \n")
    f.write("H4     "+str(x[19])+" "+str(x[20])+" "+str(x[21])+"  \n\n")
    if n < 36:
        f.write("--Link1--\n")
    n += 1
f.close()
