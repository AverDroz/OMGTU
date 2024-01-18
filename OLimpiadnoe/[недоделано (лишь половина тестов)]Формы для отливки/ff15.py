def xd(put1):
  NOT_CONNECTED = "0"
  NOT_FOUND = "1"
  X = []
  x = []
  y = []
  iw = 1

  # Ввод данных
  def input_data():
    f = open(put1, "r")
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
  def reverse(d):
    return d[10:][::-1] + d[5:10][::-1] + d[:5][::-1]

  # переворачивает деталь 
  def reverse_D(d):
    return d[10:15][::-1] + d[5:10][::-1] + d[:5][::-1] + d[15:][::-1]

  # возвращает 8 случаев расположения двух деталей
  def cases(d1, d2):
    #удаляется номер детали
    d1 = d1[:-1]
    d2 = d2[:-1]
    
    #перевёрнутые детали
    d1r = reverse(d1)
    d2r = reverse(d2)

    #8 возможных случаев
    k1 = connect(d1,d2)
    k2 = connect(d1,d2r)
    k3 = connect(d1r,d2)
    k4 = connect(d1r,d2r)
    m1 = connect(d2, d1)
    m2 = connect(d2, d1r)
    m3 = connect(d2r, d1)
    m4 = connect(d2r, d1r)
    
    return [k1,k2,k3,k4,m1,m2,m3,m4] 

  #Поиск в массиве детали
  def find(d):
    for j in allRotatedStatments(d):
      for k in j, reverse_D(j):
        if k in X:
          return k
    return NOT_FOUND

  #main
  input_data()
  while x:
    for j in cases(x[0], x[iw]):
      b = find(j)
      if b != NOT_FOUND:
        y.append(str(x[0][-1]) + " " + str(x[iw][-1]))
        x.remove(x[iw])
        x.remove(x[0])
        iw = 0
        break
    iw += 1
    
  return y

