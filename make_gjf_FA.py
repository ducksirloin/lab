# coding: UTF-8
fname1 = "FA_dih.gjf"
f = open(fname1,"w")
f.write("%mem=130MW\n")
f.write("%Chk=C:\Documents and Settings\user\デスクトップ\n")
for i in range(361):
    fname = "confamb_FA" + str(i) + ".inpcrd"
    n = 0
    f.write("#T HF/6-311G Test\n\nCOOH\n\n0 1\n")
    for f1 in open(fname,"r"):
        x = f1.split()
        if n == 2:
            f.write("C1     "+str(x[0])+" "+str(x[1])+" "+str(2)+"  \n")
            f.write("O1     "+str(x[3])+" "+str(x[4])+" "+str(5)+"  \n")
        elif n == 3:
            f.write("O2     "+str(x[0])+" "+str(x[1])+" "+str(2)+"  \n")
            f.write("H1     "+str(x[3])+" "+str(x[4])+" "+str(5)+"  \n")
        elif n == 4:
            f.write("H2     "+str(x[0])+" "+str(x[1])+" "+str(2)+"  \n\n")
        if n == 4 and i < 360:
            f.write("--Link1--\n")
        n += 1
f.close()
