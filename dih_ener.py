fname1 = "dih_side.txt"
fname2 = "ener.txt"
dih = []
ene = []
sum_dih = 72*[0]
sum_ene = 72*[0]

for f in open(fname1,"r"):
    x = f.split()
    dih.append(float(x[1]))
f.close()

for f in open(fname2,"r"):
    x = f.split()
    ene.append(float(x[1]))
f.close()

dih_ener = dict(zip(dih,ene))

for d in dih_ener:
    ang = -180
    for i in range(0,72):
        if ang <= d < ang + 5:
            sum_dih[i] += 1
            sum_ene[i] += dih_ener[d]
        ang += 5

for i in range(0,72):
    sum_ene[i] = float(sum_ene[i]) / float(sum_dih[i])
f = open("dih_ener.txt","w")
ang = -180
for i in range(0,72):
    f.write(str(ang) + " " + str(sum_ene[i]) + "\n")
    ang += 5
f.close()
