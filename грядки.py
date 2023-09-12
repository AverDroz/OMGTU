for k in (1,2,3,20):

    n=5
    m1 = 0
    m=10
    l=7
    s = 0
    print(k*(2*l+2*m+2*n)+((m+m*(k-1))*(k-1)))
    for i in range(k):
        s += 2*(m+n+l+m1)
        m1 += m
    print(s)
