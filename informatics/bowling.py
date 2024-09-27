def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(f'{prefix} Получено: {got} | Ожидалось: {expected}')

def bowling(N, hits):
    s = ['I'] * N
    hits.sort(key=lambda x: x[0])    
    for l, r in hits:
        for i in range(l - 1, r):
            s[i] = '.'
    return ''.join(s)

test(bowling(6, [(2, 4)]), 'I...II')
test(bowling(8, [(2, 4), (6, 7)]), 'I...I..I')
test(bowling(8, [(2, 5), (3, 7)]), 'I......I')
test(bowling(10, [(1, 4), (2, 5), (9, 10)]), '.....III..')