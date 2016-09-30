import math
mini = 100
v1_min = 1.9
v2_min = 2.3
QM = []

def least_square(v1, v2):
    angle = -180
    V = []
    squ = []
    global QM
    global mini
    global v1_min
    global v2_min
    for i in range(37):
        n1 = v1 * (1 + math.cos((angle / 180) * math.pi))
        n2 = 2 * v2 * (1 + math.cos((2 * angle - 180) / 180 * math.pi))
        n = n1 + n2
        V.append(n)
        angle += 10
        s = QM[i]-V[i]
        squ.append(math.pow(s, 2))

    for i in range(37):
        summ = squ[i]
        if summ < mini:
            v1_min = v1
            v2_min = v2
            mini = summ

fname = "fitting.txt"

for f in open(fname,"r"):
    x = f.split()
    QM.append(float(x[0]))

v1 = -0.6
for i in range(2000):
    v2 = 2.0
    for j in range(2000):
        least_square(v1,v2)
        v2 += 0.0001
    v1 += 0.0001

print("v1 = " + str(v1_min) + "\nv2 = " + str(v2_min) + "\nsum = " + str(mini) + "\n")
