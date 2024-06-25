 # cython: language_level=3

def factorial(num):
    """ Computes num ! """
    if num <= 1:
        return 1
    return num * factorial (num - 1)
