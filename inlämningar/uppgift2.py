"""
Redovisad: 2025-04-09
"""

def extended_list(x, n):
    """
    Funktion som skapar en lista där de element utanför listan är de första och sista index i listan.
    """
    lst = []
    for e in x:
        lst.append(e)

    for _ in range(n):
        lst.insert(0, x[0])
        lst.append(x[len(x)- 1])

    return lst

def smooth_a(x, n):
    """
    Returnerar en utjämnad version av listan x med glidande medelvärde över 2n + 1 värden.
    Listan utökas först i kanterna med hjälp av extended_list.
    """
    res = []
    extended_lst = extended_list(x, n)

    for i in range(n, len(extended_lst) - n):
        res.append(sum(extended_lst[i - n:i + n + 1])/ (2*n + 1))

    return res

def smooth_b(x, n):
    """
    Funktion som utför en medelvärdesutjämning på en lista x.
    
    För varje element i listan beräknas medelvärdet av elementet själv samt n element före
    och n element efter (så långt som möjligt inom listans gränser)
    """
    res = []

    for i in range(len(x)):
        res.append(sum(x[max(0, i - n):min(len(x), i + n + 1)]) / (min(len(x), i + n + 1) - max(0, i - n)))
    
    return res

def round_list(a_list, ndigits):
    """
    Funktion som avrundar till "n" decimaler.
    """
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
