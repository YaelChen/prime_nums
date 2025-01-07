""" This function is going through all the numbers to the given number.
A better version is at "Prime_nums-efficient.py", checking only the numbers up to the given num square root. """

def is_prime(number):
    """
    A one-liner function that checks if a given number is prime.
    :param number: a given number
    :type number: int
    :return: True/False
    :rtype: bool
    """
# the long solution:
    # for n in range(2, number):
    #     if number % n != 0:
    #         continue
    #     return False
    # return True

# One liner:
    return False if 0 in [number % n for n in range(2, number)] else True


print(is_prime(43))
