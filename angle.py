from math import *
import numpy
from matplotlib import pyplot

BULLET_WEIGHT = 0.004
CARGO_WEIGHT = 200
G = 9.8
L = 3
MEAN_SPEED = 800
POINTS = 1000
ANGLE_STD = radians(2)


def get_speed(alpha):
    return sqrt(2 * (BULLET_WEIGHT + CARGO_WEIGHT) * G * L * (1 - cos(alpha)) /
                BULLET_WEIGHT)


mean_angle = acos(1 - (BULLET_WEIGHT * MEAN_SPEED ** 2) /
                  (2 * (BULLET_WEIGHT + CARGO_WEIGHT) * G * L))
angles = numpy.random.normal(mean_angle, ANGLE_STD, POINTS).tolist()
speeds = [get_speed(angle) for angle in angles]
mean_speed = numpy.mean(speeds)
speed_std = numpy.std(speeds)
pyplot.plot(speeds, angles, 'bo')
pyplot.plot([mean_speed, mean_speed], [min(angles), max(angles)], color='red')
pyplot.plot([mean_speed - speed_std, mean_speed - speed_std],
            [min(angles), max(angles)], color='green')
pyplot.plot([mean_speed + speed_std, mean_speed + speed_std],
            [min(angles), max(angles)], color='green')
pyplot.grid(True)
pyplot.xlabel("speed")
pyplot.ylabel("angle")
pyplot.title("Mean: {0}, Std: {1}".format(mean_speed, speed_std))
pyplot.show()
