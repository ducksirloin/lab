fname1 = "AcOH_CI.txt"
fname2 = "result_Ac_CI.txt"

f = open(fname2, "w")
f.write("dihed     CI     kcal/mol\n")

a = -180
fx = open(fname1, "r")
allf = fx.read()
f1 = allf.replace("\n","")
f1 = f1.replace("\r","")
f1 = f1.replace(" ","")
x = f1.split("|")
for i in range(len(x)):
    if "CISD" in x[i]:
        n = x[i].split("=")
        kcal = float(n[1]) * 627.5095
        f.write(str(a) + " " + str(n[1]) + " " + str(kcal) + "\n")
        a += 10
