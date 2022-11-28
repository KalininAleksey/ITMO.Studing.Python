import math
from symbol import parameters

FEET_IN_YARD = 3
FEET_IN_MILE = 5280
SECONDS_IN_HOUR = 3600
DEGREES_IN_RADIAN = 180 / math.pi


def input_info():
    dist_d1 = FEET_IN_YARD * float(input("Input the shortest distance (d1) in yards between "
                                         "the lifeguard and water's broad => "))
    dist_d2 = float(input("Input the shortest distance (d2) in feet from the drowning person to the shore => "))
    dist_h = FEET_IN_YARD * float(input("Input the lateral displacement (h) in yards between"
                                        "the lifeguard and the drowning person =>"))
    speed_v_sand = FEET_IN_MILE * float(input("Input the lifeguard's speed (v_sand) in miles per "
                                              "hour => ")) / SECONDS_IN_HOUR
    coeff_n = float(input("Input the lifeguard's deceleration coefficient in water => "))
    angle_theta = float(input("Input the lifeguard's movement direction (theta) in degrees => "))
    if angle_theta >= 90 or angle_theta <= 0:
        print("The Lifeguard will never get to a drowning person. We can calculate the angle of movement direction "
              "providing the shortest time to get to drowning person")
        angle_theta = 0
    return [dist_d1, dist_d2, dist_h, speed_v_sand, coeff_n, angle_theta]


def calculate(param):
    dist_d1 = param[0]
    dist_d2 = param[1]
    dist_h = param[2]
    speed_v_sand = param[3]
    coeff_n = param[4]
    angle_theta = param[5]/DEGREES_IN_RADIAN
    dist_x = math.tan(angle_theta) * dist_d1
    dist_l1 = math.sqrt(dist_d2 ** 2 + dist_x ** 2)
    dist_l2 = math.sqrt((dist_h - dist_x) ** 2 + dist_d2 ** 2)
    return (dist_l1 + coeff_n * dist_l2) / speed_v_sand


def print_results(angle_theta, move_time):
    print(f"If lifeguard start moving at the angle theta1 {round(angle_theta)} "
          f"degrees he will reach the drowning person in {time:.1f} seconds")


parameters = input_info()
if parameters[5] == 0:
    deg_step = 1
    deg=0;
    parameters[5] = 90 - deg_step
    smallest_time = time = calculate(parameters)
    while time <= smallest_time:
        smallest_time = time
        deg += deg_step;
        parameters[5] = 90 - deg
        time = calculate(parameters)
    time = smallest_time
    parameters[5] = 90-deg+deg_step
else:
    time = calculate(parameters)
print_results(parameters[5], time)
