while True:
    a = list(map(int,input().split()))
    m_a = max(a)
    if sum(a) == 0:
        break
    a.remove(m_a)
    if a[0]**2 + a[1]**2 == m_a**2:
        print('right')
    else:
        print('wrong')
