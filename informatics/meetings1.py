def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(f'{prefix} Получено: {got} | Ожидалось: {expected}')

def meetings(a):
    a.sort(key=lambda x: x[0])
    flag = True
    for i in range(1, len(a)):
        if a[i][0] < a[i - 1][1]:
            return False
    return True

test(meetings([(2,3), (5,7), (4,5)]), True)
test(meetings([(2,3), (5,7), (4,6)]), False)
test(meetings([(2,3), (2,4)]), False)

