#coding: UTF-8

def max(x):#最大値の取得
    max = x[0]
    for i in range(1,10001):
        if max < x[i]:
            max = x[i]
    return max

def min(x):#最小値の取得
    min = x[0]
    for i in range(1,10001):
        if min > x[i]:
            min = x[i]
    return min

x = input('Read line : ')#読み込む行の指定
n = input('Step size : ')#ヒストグラムの刻み幅の指定
t = 10001
data = t*[0]
i = 0
fname = "ener0.xvg"
for f in open(fname,"r"):#ファイル読み込み
    ener = f.split()
    data[i] = float(ener[x])
    i += 1

max = max(data)
min = min(data)

fname2 = raw_input("What's the name of the output file? : ")#出力ファイルの指定
f = open(fname2,"w")
j = 0
hist = 10000*[0]
hmin = min
hmax = hmin + n
while hmin <= max:
    for i in range(10001):
        if hmin <= data[i] < hmax:
            hist[j] += 1
    f.write(str(hist[j]) + "\n")#出力ファイルへの書き込み
    hmin += n
    hmax += n
    j += 1

print "\n" + fname2 + " was generated!"
