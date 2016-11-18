fname1 = "AcOH_MP2.txt"
fname2 = "result_Ac_MP2.txt"

f = open(fname2, "w")
f.write("dihed     MP2     kcal/mol\n")

a = -180
for fx in open(fname1, "r"):
    y = fx.split("|")
    for i in range(len(y)):
        if "MP2=" in y[i]:
            x = y[i].split("=")
    kcal = float(x[1]) * 627.5095
    f.write(str(a) + " " + str(x[1]) + " " + str(kcal) + "\n")
    a += 10
