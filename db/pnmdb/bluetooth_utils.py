def rssi_to_integer(rssi):
    i = rssi.rstrip(' dBm')
    return int(i)


def rssi_to_meters(measured_rssi):
    rssi_at_one_meter = -40
    pathloss_exponent = 2.2
    distance = (10 * (rssi_at_one_meter - measured_rssi)) / (10 * pathloss_exponent)
    return round(distance, 2)
