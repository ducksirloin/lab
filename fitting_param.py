import math

fname = "fitting.txt"
QM = [0]*37
i = 0
for f in open(fname,"r"):
    x = f.split()
    QM[i] = float(x[0])
    i += 1

mini = 100
v1_min = 1.9
v2_min = 2.3

V = [0]*37
squ = [0]*37

v1 = -0.6000
for i in range(2000):
    v2 = 2.0000
    angle = -180
    for j in range(2000):
        for i in range(37):
            n1 = v1 * (1 + math.cos((angle / 180) * math.pi))
            n2 = 2 * v2 * (1 + math.cos((2 * angle - 180) / 180 * math.pi))
            n = n1 + n2
            V[i] = n
            angle += 10
            s = QM[i]-V[i]
            squ[i] = math.pow(s, 2)
        summ = 0
        for k in range(37):
            summ += squ[k]
        if summ < mini:
            v1_min = v1
            v2_min = v2
            mini = summ
        v2 += -0.0001
    v1 += 0.0001



print("v1 = " + str(v1_min) + "\nv2 = " + str(v2_min) + "\nsum = " + str(mini) + "\n")
