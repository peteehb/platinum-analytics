
# Equation of a normal circle = x^2 + y^2 - r^2 = 0
# Equation of a cirle = x^2 + y^2 + 2gx + 2fy + c = 0


class Sensor:
    pos_x = 0
    pos_y = 0

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y


class Receiver:
    pos_x = 0
    pos_y = 0
    radius = 0

    def __init__(self, x, y, r):
        self.pos_x = x
        self.pos_y = y
        self.radius = r


# Should not be needed if r1 is already normalized
def normalize_sensor(r1, r2):
    r2.pos_x = r2.pos_x - r1.pos_x
    r2.pos_y = r2.pos_y - r1.pos_y
    return r2


def calculate_sensor_x(r2, r3):
    x = ((r3.radius**2)-(r2.radius**2))/(4 * r2.pos_x)
    return x


def calculate_sensor_y(rec1, rec2, rec3, sensor_x):
    x = sensor_x
    g = rec2.pos_x
    f = -rec2.pos_y
    r1 = rec1.radius
    r3 = rec3.radius

    # x^2 + y^2 - r^2 = 0
    # y^2 = r^2 - x^2
    sensor_y_square = (r1**2) - (x**2)

    # (sensor_x**2) + sensor_y_square + (2*rec2.pos_x*sensor_x) + (2*rec2.pos_y*sensor_y) + (rec2.pos_x**2) + (rec2.pos_y**2) - (rec3.radius**2)
    # In terms of y.. y = -1/2f(x^2 + y^2 + 2gx + g^2 + f^2 - r3^2)
    y = -(1/2*f)*(x**2 + sensor_y_square + 2*g*x + g**2 + f**2 - r3**2)
    return y


def main():

    rec1 = Receiver(20, 20, 10)
    rec2 = Receiver(-45, 20, 50)
    rec3 = Receiver(22, 20, 30)

    x = calculate_sensor_x(rec2, rec3)
    y = calculate_sensor_y(rec1, rec2, rec3, x)

    sensor = Sensor(x, y)
    print sensor.pos_x, sensor.pos_y

if __name__ == "__main__":
    main()
