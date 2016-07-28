fname = "ener.out.xvg"
fname2 = "charm_ener.txt"
#name = []
#for i in range(361):
#    name.append("ener"+ str(i) + ".out.xvg")

f2 = open(fname2,"w")
#for i in range(361):
#    fname = name[i]
f = open(fname,"r")
x = f.readline()
ener = x.split()
for i in range(len(ener)):
    f2.write(ener[i] + " ")
f2.write("\n")
f2.close()
