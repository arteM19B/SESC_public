def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(f'{prefix} Получено: {got} | Ожидалось: {expected}')



def meetings2(a):
    a.sort(key=lambda x: x[0])
    cnt = 1
    for i in range(1, len(a)):
        if a[i][0] < a[i - 1][1]:
            cnt += 1
    return cnt

test(meetings2([(2,3), (5,7), (4,5)]), 1)
test(meetings2([(2,3), (5,7), (4,6)]), 2)
test(meetings2([(2,3), (2,4)]), 2)
test(meetings2([(2,8), (5,7), (4,6)]), 3)