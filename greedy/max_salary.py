def max_salary(n_ints, *args):
    """

    :param n_ints: int: num of arguments
    :param args: integers
    :return: max int comprised of *args
    """
    if n_ints < 1 or n_ints > 100:
        raise ValueError('num of integers out of range [1, 100]!')


    numbers = list(args)
    res = []

    while len(numbers) > 0:
        max_num = -1
        max_num_id = -1
        for i,n in enumerate(numbers):
            if n >= max_num:
                max_num = n
                max_num_id = i
        res.append(max_num)
        numbers.pop(max_num_id)

    return res


if __name__ == '__main__':
    print(max_salary(2, 21, 2
                     ))

    print(max_salary(
        5, 9, 4, 6, 1, 9
    ))

    print(max_salary(
        3, 23, 39, 92
    ))





