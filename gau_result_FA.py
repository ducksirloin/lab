fname1 = "FA_nuclear.txt"
fname2 = "FA_SCF.txt"
fname3 = "result_gau_FA.txt"
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
f.write("dihed     nuclear     SCF     sum     kcal/mol\n")
for i in range(361):
    s = float(nuc[i]) + float(SCF[i])
    kcal = s *  627.5095
    f.write(str(a) + " " + str(nuc[i]) + " " + str(SCF[i]) + " " + str(s) + " " + str(kcal) + "\n")
    a += 1
f.close()
