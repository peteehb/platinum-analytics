import math


class Bluetooth(object):
    def __init__(self, wavelength):
        # Rssi values for distances of 1 - 10m
        self.rssi_conversion_table = [-44.8, -47.7, -48.7, -53.1, -55.6, -61.8, -67.2, -66.5, -69.0]
        self.wavelength = wavelength

    def rssi_to_meters(self, rssi):
        if rssi in self.rssi_conversion_table:
            return self.rssi_conversion_table.index(rssi) + 1
        else:
            return 0

    def signal_propagation(self, beacon, node):
        t = node.transmission_power
        gt = node.signal_gain
        gr = beacon.signal_gain
        w = self.wavelength
        d = distance(node, beacon)

        return ((t*gt*gr*w) ** 2) / ((4 * 3.14 * d) ** 2)


class Beacon(object):
    def __init__(self, pos_x, pos_y, r, rssi=None, signal_gain=None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.node_rssi = rssi
        self.node_distance = r.rssi_to_meters(r, self.node_rssi)
        self.signal_propagation = 0
        self.signal_gain = signal_gain

class Node(object):
    def __init__(self, signal_gain, transmission_power, pos_x=None, pos_y=None, blind=True):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.blind = blind
        self.signal_gain = signal_gain
        self.transmission_power = transmission_power

    def position(self, b1, b2, b3):
        va = (((b2.node_distance ** 2) - (b3.node_distance ** 2)) - ((b2.pos_x ** 2) - (b3.pos_x ** 2))
              - ((b2.pos_y ** 2) - (b3.pos_y ** 2))) / 2

        vb = (((b2.node_distance ** 2) - (b1.node_distance ** 2)) - ((b2.pos_x ** 2) - (b1.pos_x ** 2))
              - ((b2.pos_y ** 2) - (b1.pos_y ** 2))) / 2

        self.pos_y = (((vb * (b3.pos_x - b2.pos_x)) - (va * (b1.pos_x - b2.pos_x)))
                      / (((b1.pos_y - b2.pos_y) * (b3.pos_x - b2.pos_x))
                         - ((b3.pos_y - b2.pos_y) * (b1.pos_x - b2.pos_x))))

        self.pos_x = (va - (self.pos_y * (b3.pos_y - b2.pos_y))) / (b3.pos_x - b2.pos_x)

        self.blind = False


def distance(p1, p2):
    return math.sqrt(((p2.pos_x - p1.pos_x) ** 2) + ((p2.pos_y - p1.pos_y) ** 2))


def output(*args, **kwargs):
    delimiter = ' '
    d_length = len(delimiter)

    if 'delimiter' in kwargs:
        delimiter = kwargs['delimiter']

    text = ''
    for arg in args:
        text += str(arg) + delimiter

    text = text[:-d_length]
    print ("Test output: " + text)


def main():
    r = Bluetooth(wavelength=10)

    b1 = Beacon(0, 10, -47.7, r)
    b2 = Beacon(5, 0, -47.7, r)
    b3 = Beacon(10, 10, -47.7, r)

    output(distance(b1, b2))
    output(distance(b1, b3))
    output(distance(b2, b3))

    n1 = Node(signal_gain=0, transmission_power=0)
    n1.position(b1, b2, b3)

    b1.signal_propagation = r.signal_propagation(b1, n1)
    b2.signal_propagation = r.signal_propagation(b2, n1)
    b3.signal_propagation = r.signal_propagation(b3, n1)

    output(n1.pos_x, n1.pos_y, delimiter=',')


main()
