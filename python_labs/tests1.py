def test(n):
    try:
        num = int(n)
        return 0
    except:
        print('нельзя преобразовать в число')
        return 1

def tests():
    test_result = 0
    print('test 1')
    test_result = test_result + test([1])
    print('test 2')
    test_result = test_result + test('-1')
    print('test 3')
    test_result = test_result + test([{1}])
    print('test 4')
    test_result = test_result + test('l')
    print('test 5')
    test_result = test_result + test(-1)
    print('test 6')
    test_result = test_result + test(1.0)
    if test_result == 0:
        print("ошибок нет")
    else:
        print('количество ошибочных тестов',test_result)