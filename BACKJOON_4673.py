def df():
    a = []
    for n in range(10000):
        k = n
        if n > 1000:
            k = k + int(n/1000)
            n = n % 1000
        if n >= 100:
            k = k + int(n/100)
            n = n % 100
        if n >= 10:
            k = k + int(n/10)
            n = n % 10
        k = k + n
        a.append(k)
    for m in range(10000):
        if m not in a:
            print(m)

df()