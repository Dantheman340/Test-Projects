def distance_from_zero(distance):
    distance = -5
    if type(distance) == int or type(distance) == float:
        return abs(distance)
    else:
        return "Nope"
