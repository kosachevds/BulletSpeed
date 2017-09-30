import numpy
import math
from matplotlib import pyplot

BULLET_WEIGHT = 0.004
CARGO_WEIGHT = 1.0
SPRING_CONST = 50
MEAN_SPEED = 800.0
STD_DIFF = 0.01
G = 9.8
POINTS = 1000
ENERGY_RATIO = BULLET_WEIGHT / (BULLET_WEIGHT + CARGO_WEIGHT)
WEIGHT_SUM = CARGO_WEIGHT + BULLET_WEIGHT


def get_speed(height):
    return math.sqrt(
        (SPRING_CONST * height ** 2 + 2 * WEIGHT_SUM * G * height) /
        (ENERGY_RATIO * BULLET_WEIGHT))


mean_diff = math.sqrt(
    (WEIGHT_SUM * G / SPRING_CONST) ** 2 +
    ENERGY_RATIO * BULLET_WEIGHT * MEAN_SPEED ** 2 / SPRING_CONST) - \
            WEIGHT_SUM * G / SPRING_CONST
diffs = numpy.random.normal(mean_diff, STD_DIFF, POINTS).tolist()
speeds = [get_speed(d) for d in diffs]
mean_speed = numpy.mean(speeds)
speed_std = numpy.std(speeds)

pyplot.plot(speeds, diffs, 'bo')
pyplot.plot([mean_speed, mean_speed], [min(diffs), max(diffs)], color='red')
pyplot.plot([mean_speed - speed_std, mean_speed - speed_std],
            [min(diffs), max(diffs)], color='green')
pyplot.plot([mean_speed + speed_std, mean_speed + speed_std],
            [min(diffs), max(diffs)], color='green')
pyplot.grid(True)
pyplot.xlabel("speed")
pyplot.ylabel("time")
pyplot.title("Mean: {0}, Std: {1}".format(mean_speed, speed_std))
pyplot.show()
