def car_fueling(d, m, n, *args):
    """

    :param d:
    :param m:
    :param n:
    :param args:
    :return:
    """

    num_refills = 0
    distance_left = d

    # safe move -- refill at farthest stop possible to
    # travel w/out a refill


    prev_stop = 0

    for i,stop in enumerate(args):
        if m > stop - prev_stop:
            best_stop = stop

        else:
            num_refills += 1
            prev_stop = stop
            distance_left -= stop

    if distance_left > m:
        return -1
    else:
        return num_refills


if __name__ == '__main__':
    print(car_fueling(950, 400, 4, 200, 375, 550, 750))

