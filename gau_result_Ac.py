fname1 = "AcOH_nuclear.txt"
fname2 = "AcOH_SCF.txt"
fname3 = "result_gau_Ac.txt"
nuc = []
SCF = []

for f in open(fname1, "r"):
    x = f.split()
    nuc.append(x[3])

for f in open(fname2, "r"):
    x = f.split()
    SCF.append(x[4])

a = -180
f = open(fname3, "w")
f.write("dihed     nuclear     SCF     sum     kcal/mol     nuclear*627     SCF*627\n")
for i in range(37):
    s = float(nuc[i]) + float(SCF[i])
    kcal = s *  627.5095
    nu = float(nuc[i]) * 627.5095
    sc = float(SCF[i]) * 627.5095
    f.write(str(a) + " " + str(nuc[i]) + " " + str(SCF[i]) + " " + str(s) + " " + str(kcal) + " " + str(nu) + " " + str(sc) + "\n")
    a += 10
f.close()
