a = -180
fname1 = "FA_dih.gjf"
f = open(fname1,"w")
f.write("%mem=130MW\n")
f.write("%Chk=C:\usr\n")
for i in range(5):
    fname = "HCOOH.inpcrd"
    n = 0
    f.write("#T HF/6-311G Test\n\nCOOH\n\n0 1\n")
    for f1 in open(fname,"r"):
        x = f1.split()
        if n == 2:
            f.write("C1     "+str(round(float(x[0]), 3))+" "+str(round(float(x[1]), 3))+" "+str(round(float(x[2]), 3))+"  \n")
            f.write("O1     "+str(round(float(x[3]), 3))+" "+str(round(float(x[4]), 3))+" "+str(round(float(x[5]), 3))+"  \n")
        elif n == 3:
            f.write("O2     "+str(round(float(x[0]), 3))+" "+str(round(float(x[1]), 3))+" "+str(round(float(x[2]), 3))+"  \n")
            f.write("H1     "+str(round(float(x[3]), 3))+" "+str(round(float(x[4]), 3))+" "+str(round(float(x[5]), 3))+"  \n")
        elif n == 4:
            f.write("H2     "+str(round(float(x[0]), 3))+" "+str(round(float(x[1]), 3))+" "+str(round(float(x[2]), 3))+"  \n\n")
        if n == 4 and i < 4:
            f.write("--Link1--\n")
        n += 1
