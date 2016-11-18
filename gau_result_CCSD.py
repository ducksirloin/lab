fname1 = "AcOH_CCSD.txt"
fname2 = "result_Ac_CCSD.txt"

f = open(fname2, "w")
f.write("dihed     CCSD     kcal/mol\n")

a = -180
for fx in open(fname1, "r"):
    y = fx.split("|")
    for i in range(len(y)):
        if "CCSD(T)" in y[i]:
            x = y[i].split("=")
    kcal = float(x[1]) * 627.5095
    f.write(str(a) + " " + str(x[1]) + " " + str(kcal) + "\n")
    a += 10
