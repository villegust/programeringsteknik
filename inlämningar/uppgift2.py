def smooth_a(a, n):
    r = []
    r.append(a[0])

    for i in range(1, len(a)-1):
        r.append(1/(2*n+1)*sum(a[i-n:i+n]))

    r.append(a[-1])

    return r

x = [1, 2, 6, 4, 5, 0, 1, 2] #En lista på icke-negativa  tal

print(f"smooth_a(x, 1): {smooth_a(x, 1)}")