def xd(put1):
  NOT_CONNECTED = "0"
  NOT_FOUND = "1"
  X = []
  x = []
  y = []
  global N
  N = 0
  
  # Ввод данных
  def input_data():
    f = open(put1, "r")
    global N
    N = int(f.readline())
    for i in range(N):
        X.append(f.readline().split())
    for i in range(2*N):
        # К половинкам деталей в конец добавляется их номер
        b = (f.readline() + " " + str(i+1)).split()
        x.append(b)

  # Вывод 4 случаев вращения детали
  def allRotatedStatments(d):
    p1 = d[:5] 
    p2 = d[5:10]
    p3 = d[10:15]
    p4 = d[15:]
    d1 = p1 + p2 + p3 + p4
    d2 = p2 + p3 + p4 + p1
    d3 = p3 + p4 + p1 + p2
    d4 = p4 + p1 + p2 + p3
    return [d1,d2,d3,d4]
    
  # Соединение двух половинок в деталь напрямую
  def connect(d1,d2):
    if (d1[:5] == d2[:5][::-1] and d1[10:] == d2[10:][::-1]):
      return d1[:5] + d2[5:10][::-1] + d1[10:] + d1[5:10]
    return NOT_CONNECTED

  # переворачивает часть детали
  def partReverse(d):
    return d[10:][::-1] + d[5:10][::-1] + d[:5][::-1]

  # переворачивает деталь 
  def detailReverse(d):
    return d[10:15][::-1] + d[5:10][::-1] + d[:5][::-1] + d[15:][::-1]

  # возвращает 8 случаев расположения двух деталей
  def cases(d1, d2):
    #удаляется номер детали
    d1 = d1[:-1]
    d2 = d2[:-1]
    
    #перевёрнутые детали
    d1r = partReverse(d1)
    d2r = partReverse(d2)

    #8 возможных случаев
    k1 = connect(d1,d2)
    k2 = connect(d1,d2r)
    k3 = connect(d1r,d2)
    k4 = connect(d1r,d2r)
    m1 = connect(d2, d1)
    m2 = connect(d2, d1r)
    m3 = connect(d2r, d1)
    m4 = connect(d2r, d1r)

    result = []
    for i in [k1,k2,k3,k4,m1,m2,m3,m4]:
      if i != NOT_CONNECTED:
        result.append(i)
    
    return result 

  #Поиск в массиве детали
  def find(d):
    for j in allRotatedStatments(d):
      for k in j, detailReverse(j):
        if k in X:
          return k
    return NOT_FOUND

  #main
  input_data()
  for i in range(len(x)): #поиск всех совпадающих в данные детали половинок
    for j in range(i+1, len(x)):
      for k in cases(x[i], x[j]):
        b = find(k)
        if b != NOT_FOUND:
          y.append([i+1, j+1])
          break
  
  if len(y) == N: # всё хорошо
    return set(str(i[0]) + " " + str(i[1]) for i in y)
  if len(y) < N: # всё плохо
    return set(["hyinya kakaeto"])
  else: # как минимум 1 деталь можно получить различными вариантами половинок
    FH = [i[0] for i in y]
    SH = [i[1] for i in y]
    Nums = []
    k = 0
    #print(y)
    for i in range(len(y) - 1):
      if i-k >= len(y) - 1:
        break
      if y[i-k][0] in Nums or y[i-k][1] in Nums:
        y.pop(i-k)
        k += 1
        continue
      if y[i-k][0] == y[i-k+1][0]:
        if (FH.count(y[i-k][1]) == 0) and (SH.count(y[i-k][1]) == 1):
          Nums.append(y[i-k][0])
          Nums.append(y[i-k][1])
          y.pop(i-k+1)
        else:
          Nums.append(y[i-k+1][0])
          Nums.append(y[i-k+1][1])
          y.pop(i-k)
      else:
        Nums.append(y[i-k][0])
        Nums.append(y[i-k][1])
    if y[-1][0] in Nums or y[-1][1] in Nums:
      y.pop(-1)
    #print(y)
    #print(len(y), N)
    return set(str(i[0]) + " " + str(i[1]) for i in y)