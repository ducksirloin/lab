sum_cyn = 0.0
sum_anti = 0.0
fname = "dih_side.txt"
for f in open(fname,"r"):
    data = f.split()
    dih = float(data[1])
    if -90.0 < dih <90.0:
        sum_cyn += 1
    else:
        sum_anti += 1

ave_cyn = sum_cyn / 10000.0
ave_anti = sum_anti / 10000.0

print "ave_cyn = %lf" % ave_cyn
print "ave_anti = %lf" % ave_anti
