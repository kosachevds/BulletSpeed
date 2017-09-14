from math import *
import numpy
import matplotlib.pyplot as pyplot

SPEED = 800
HEIGHT = 1
G = 9.8
POINTS = 1000 
DISTANCE_STD = 5


def get_speed(distance):
    return distance / sqrt(2 * HEIGHT / G)


mean_distance = sqrt(2 * HEIGHT / G) * SPEED
distances = numpy.random.normal(mean_distance, DISTANCE_STD, POINTS).tolist()
speeds = [get_speed(d) for d in distances]

mean_speed = numpy.mean(speeds)
std_speed = numpy.std(speeds)

pyplot.plot(speeds, distances, 'bo')
pyplot.plot([mean_speed, mean_speed], [min(distances), max(distances)],
            color='red')
pyplot.plot([mean_speed - std_speed, mean_speed - std_speed],
            [min(distances), max(distances)], color='green')
pyplot.plot([mean_speed + std_speed, mean_speed + std_speed],
            [min(distances), max(distances)], color='green')
pyplot.grid(True)
pyplot.xlabel("speed")
pyplot.ylabel("distance")
pyplot.title("Mean: {0}, Std: {1}".format(mean_speed, std_speed))
pyplot.show()
