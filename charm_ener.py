fname2 = "charm_ener.txt"
name = []
for i in range(4):
    name.append("ener"+ str(i) + ".out.xvg")
a = -180
f2 = open(fname2,"w")
f2.write("dihed_angle Proper-Dih Improper-Dih GB-Polarization Coulomb-14 Potential Kinetic-En Total-Energy\n")
for i in range(4):
    fname = str(name[i])
    f = open(fname,"r")
    x = f.readline()
    ener = x.split()
    f2.write(str(a) + " ")
    a += 1
    for i in range(1,len(ener)):
        f2.write(ener[i] + " ")
    f2.write("\n")
f2.close()
