import math

radius = 50
x_center = 50
y_center = 50


def is_point_in_circle(x: int, y: int) -> bool:
    distance_squared = (x-x_center)*(x-x_center) + (y-y_center)*(y-y_center)
    return True if distance_squared < radius*radius else False


def is_black(percentage: int, x: int, y: int) -> bool:
    if not is_point_in_circle(x, y):
        return False
    if percentage == 0:
        return False

    pie_angle = float(percentage)/100*360
    point_angle = math.degrees(math.atan2(y-y_center, x-x_center))

    while point_angle < 0:
        point_angle += 360

    return pie_angle >= point_angle
