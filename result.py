fname = "allout.txt"
fname1 = "Etot.txt"
fname2 = "EPtot.txt"
fname3 = "BOND.txt"
fname4 = "ANGLE.txt"
fname5 = "DIHED.txt"
fname6 = "1-4NB.txt"
fname7 = "1-4EEL.txt"
fname8 = "VDWAALS.txt"
fname9 = "EELEC.txt"
f1 = open(fname1,"w")
f2 = open(fname2,"w")
f3 = open(fname3,"w")
f4 = open(fname4,"w")
f5 = open(fname5,"w")
f6 = open(fname6,"w")
f7 = open(fname7,"w")
f8 = open(fname8,"w")
f9 = open(fname9,"w")

ang = [-180]*9
for f in open(fname,"r"):
    x = f.split()
    for i in range(len(x)):
        if x[i] == "Etot":
            f1.write(str(ang[0]) + " " + str(x[i+2]) + "\n")
            ang[0] += 1
        elif x[i] == "EPtot":
            f2.write(str(ang[1]) + " " + str(x[i+2]) + "\n")
            ang[1] += 1
        elif x[i] == "BOND":
            f3.write(str(ang[2]) + " " + str(x[i+2]) + "\n")
            ang[2] += 1
        elif x[i] == "ANGLE":
            f4.write(str(ang[3]) + " " + str(x[i+2]) + "\n")
            ang[3] += 1
        elif x[i] == "DIHED":
            f5.write(str(ang[4]) + " " + str(x[i+2]) + "\n")
            ang[4] += 1
        elif x[i] == "1-4NB":
            f6.write(str(ang[5]) + " " + str(x[i+2]) + "\n")
            ang[5] += 1
        elif x[i] == "1-4EEL":
            f7.write(str(ang[6]) + " " + str(x[i+2]) + "\n")
            ang[6] += 1
        elif x[i] == "VDWAALS":
            f8.write(str(ang[7]) + " " + str(x[i+2]) + "\n")
            ang[7] += 1
        elif x[i] == "EELEC":
            f9.write(str(ang[8]) + " " + str(x[i+2]) + "\n")
            ang[8] += 1
