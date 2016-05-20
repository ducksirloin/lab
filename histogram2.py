def max(x):
    max = x[0]
    for i in range(1,10001):
        if max < x[i]:
            max = x[i]
    return max

def min(x):
    min = x[0]
    for i in range(1,10001):
        if min > x[i]:
            min = x[i]
    return min

x = input('Read line : ')
n = input('Step size : ')
t = 10001
data = t*[0]
i = 0
fname = "ener0.xvg"
for f in open(fname,"r"):
    ener = f.split()
    data[i] = float(ener[x])
    i += 1

max = max(data)
min = min(data)

fname2 = raw_input("What's the name of the output file? : ")
if fname2 != "no":
    f = open(fname2,"w")
j = 0
hist = 1000*[0]
hmin = min
hmax = hmin + n
while hmin <= max:
    for i in range(10001):
        if hmin <= data[i] < hmax:
            hist[j] += 1
    if fname2 == "no":
        print "%lf %d" % (hmin,hist[j])
    elif fname2 != "no":
        f.write(str(hmin) + " " + str(hist[j]) + "\n")
    hmin += n
    hmax += n
    j += 1
if fname2 != "no":
    print "\n" + fname2 + " has been made!"
