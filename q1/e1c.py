def is_prime(p: int) -> bool:
    """
    Return whether a number is prime
    :param p: int - the number to validate
    :return: boolean - True if the number is prime, False otherwise
    """

    return not any(i for i in range(2, p) if p % i == 0)


if __name__ == '__main__':
    print(is_prime(10))
    print(is_prime(13))
