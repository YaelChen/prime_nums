import math


def prime_num(num):
    """
    a function to calculate if a given number is a prime number, by dividing it by all the numbers from 2 to the number's square root.
    :param num: an integer to check if it is prime or not.
    :type: int
    :return: True if prime, False is not
    :rtype: Bool
    """
    print(round(math.sqrt(num)))
    print(math.sqrt(num))
    for n in range(2, round(math.sqrt(num))+1):
        print(n)
        if num % n == 0:
            return False
    return True


print(prime_num(6700417))
