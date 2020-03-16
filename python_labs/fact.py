from tests1 import *

def factorial(x):
    if x>0:
        return factorial(x-1)*x
    if x == 0:
        return 1


def main():
    num = input()
    test_result = test(num)
    if test_result == 0:
        print(factorial(int(num)))

main()
tests()

'''
>>> factorial(5)
120
>>> factorial(1)
1
>>> factorial(0)
1
>>> factorial(-1)
err
>>> factorial('-1')
err2
'''
#if __name__ == '__main__':
import doctest
doctest.testmod()
