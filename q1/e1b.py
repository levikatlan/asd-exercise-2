def sieve_of_eratosthenes(n: int):
    """
    returns a set of all the primes up to a certain number

    :param n: the given number up to which to get all the primes
    :return: a set of all the primes up to n
    """
    return {i for i in range(2, n) if 0 not in [i % j for j in range(2, i)]}


if __name__ == '__main__':
    print(sieve_of_eratosthenes(100))
