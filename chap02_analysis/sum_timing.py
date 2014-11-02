import time

__author__ = 'darryl'


def sum_of_n_2(n):
    start = time.time()
    result = 0
    for i in range(1, n + 1):
        result += i
    end = time.time()
    return result, end - start


def ref_sum_of_n_2(n):
    start = time.time()
    result = sum(i for i in range(1, n+1))
    end = time.time()
    return result, end - start


def sum_of_n_3(n):
    start = time.time()
    result = (n * (n + 1)) / 2
    end = time.time()
    return result, end - start


if __name__ == "__main__":
    for i in range(5):
        print("Sum is %d required %f seconds" % sum_of_n_2(10000*(10**i)))
    for i in range(5):
        print("Refactored sum of n2 is %d required %f seconds" % ref_sum_of_n_2(10000*(10**i)))
    for i in range(5):
        print("Sum of n3 is %d required %f seconds" % ref_sum_of_n_2(10000*(10**i)))