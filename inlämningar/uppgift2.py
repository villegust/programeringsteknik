def extended_list(x, n):
    lst = []
    for e in x:
        lst.append(e)

    for _ in range(n):
        lst.insert(0, x[0])
        lst.append(x[len(x)- 1])

    return lst

def smooth_a(x, n):
    res = []
    y = extended_list(x, n)

    for i in range(n, len(y) - n):
        res.append(sum(y[i-n:i+1+n])/ (2*n + 1))

    return res

def smooth_b(x, n):
    res = []

    for i in range(len(x)):
        res.append(sum(x[max(0, i - n):min(len(x), i + n + 1)]) / (min(len(x), i + n + 1) - max(0, i - n)))

    return res

def round_list(a_list, ndigits):
    res = []
    for i in a_list:
        res.append(round(i, ndigits))

    return res

x = [1, 2, 6, 4, 5, 0, 1, 2]
print('smooth_a(x, 1): ', smooth_a(x, 1))
print('smooth_a(x, 2): ', smooth_a(x, 2))
print('smooth_b(x, 1): ', smooth_b(x, 1))
print('smooth_b(x, 2): ', smooth_b(x, 2))
print('smooth_a(x, 1) rounded: ', round_list(smooth_a(x, 1), 2))
