#distance = -5.0
#print(type(distance))
#print(abs(distance))

distance = -5
def distance_from_zero(distance):
    if type(distance) == int or type(distance) == float:
        return abs(distance)
    else:
        return "Nope"
