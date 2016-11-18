fname1 = "AcOH_CI.txt"
fname2 = "result_Ac_CI.txt"

f = open(fname2, "w")
f.write("dihed     CI     kcal/mol\n")

a = -180
p = 1
for fx in open(fname1, "r"):
    if p == 1:
        y1 = fx.split("|")
        p += 1
    elif p == 2:
        y2 = fx.split("|")
        y3 = y1.extend(y2[0])
        print y3
        y4 = map(str, y3)
        y = "".join(y4)
        x = y.split("=")
        f.write(str(a) + " " + str(x[6]) + "\n")
        a += 10
        p += 1
    elif p == 3:
        p = 1
