fname1 = "Etot.txt"
fname2 = "EPtot.txt"
fname3 = "BOND.txt"
fname4 = "ANGLE.txt"
fname5 = "DIHED.txt"
fname6 = "1-4NB.txt"
fname7 = "1-4EEL.txt"
fname8 = "VDWAALS.txt"
fname9 = "EELEC.txt"

Etot = []
EPtot = []
BOND = []
ANGLE = []
DIHED = []
NB = []
EEL = []
VDWAALS = []
EELEC = []

for f in open(fname1,"r"):
    x = f.split()
    Etot.append(x[1])
for f in open(fname2,"r"):
    x = f.split()
    EPtot.append(x[1])
for f in open(fname3,"r"):
    x = f.split()
    BOND.append(x[1])
for f in open(fname4,"r"):
    x = f.split()
    ANGLE.append(x[1])
for f in open(fname5,"r"):
    x = f.split()
    DIHED.append(x[1])
for f in open(fname6,"r"):
    x = f.split()
    NB.append(x[1])
for f in open(fname7,"r"):
    x = f.split()
    EEL.append(x[1])
for f in open(fname8,"r"):
    x = f.split()
    VDWAALS.append(x[1])
for f in open(fname9,"r"):
    x = f.split()
    EELEC.append(x[1])

a = -180
fname10 = "all_result.txt"
f = open(fname10,"w")
f.write("dih_angle Etot EPtot BOND ANGLE DIHED 1-4NB 1-4EEL VDWAALS EELEC\n")
for i in range(0,361):
    f.write(str(a) + " " + str(Etot[i]) + " " + str(EPtot[i]) + " " + str(BOND[i]) + " " + str(ANGLE[i]) + " " + str(DIHED[i]) + " " + str(NB[i]) + " " + str(EEL[i]) + " " + str(VDWAALS[i]) + " " + str(EELEC[i]) + "\n")
    a += 1
