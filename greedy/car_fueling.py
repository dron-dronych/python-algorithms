# You are going to travel to another city that is located 𝑑 miles away from your home city.
# Your car can travel at most 𝑚 miles on a full tank and you start with a full tank. Along your way,
# there are gas stations at distances stop1, stop2, . . . , stop𝑛 from your home city.
# What is the minimum number of refills needed?


def car_fueling(distance, capacity, n_stations, *args):
    """
    find min number of refills along travel distance

    :param distance: int: distance to travel
    :param capacity: int: full tank capacity
    :param n_stations: int: num of gas stations along the way
    :param args: gas stations at distance arg1, arg2,..., argn along the way
    :return: int: min number of refills to travel distance
    """

    num_refills = 0
    distance_left = distance

    # safe move -- refill at farthest stop possible to
    # travel w/out a refill
    stops = [arg for arg in args]
    stops.append(distance)  # last point on the route

    prev_refill = 0
    prev_stop = 0

    for stop in stops:
        if capacity < stop - prev_stop:
            return -1
        if capacity > stop - prev_refill:
            prev_stop = stop

        else:
            num_refills += 1
            prev_refill = prev_stop
            distance_left -= stop

    return num_refills


if __name__ == '__main__':
    print(car_fueling(950, 400, 4, 200, 375, 550, 750))
    print(car_fueling(10, 3, 4, 1, 2, 5, 9))
    print(car_fueling(200, 250, 2, 100, 150))

