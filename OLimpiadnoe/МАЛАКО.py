f = open("input8.txt", "r")
N = int(f.readline())
x = [i for i in f.read().split("\n")]
y = []
for j in x:
    i = [ float(i) for i in j.split() ]
    i[0] = i[0] / 10
    i[1] = i[1] / 10
    i[2] = i[2] / 10
    i[3] = i[3] / 10
    i[4] = i[4] / 10
    i[5] = i[5] / 10
    u1 = 2 * i[0] * i[1] + 2 * i[1] * i[2] + 2 * i[0] * i[2]
    u2 = 2 * i[3] * i[4] + 2 * i[3] * i[5] + 2 * i[4] * i[5]
    m1 = i[0] * i[1] * i[2]
    m2 = i[3] * i[4] * i[5]
    y.append((u2 * i[6] - u1 * i[7]) / (u2*m1 - u1*m2))

print(y.index(min(y))+1, round(min(y), 2))