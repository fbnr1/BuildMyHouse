import GUI.gui


def construct_building():
    a = building_constructable()
    if a:
        pass  # code zum konstruieren des Gebäudes


def building_constructable():
    a = windows_valid()
    b = width_and_height_valid()
    c = collision()
    d = roofheight_not_higher_than_buildingheight()
    e = window_not_bigger_than_wall()
    return a and b and c and d and e


def windows_valid(window_count, wall_width, wall_len):

    return True


def width_and_height_valid(wall_len, wall_width):
    if wall_width != 0 and wall_len != 0:
        return True


def roofheight_not_higher_than_buildingheight(wall_width, roofheight):
    if wall_width > roofheight:
        return True


def collision(object1, object2):
    pass  # if object1.pos != object2.pos --> return True, 2 Objekte sollen nicht die gleiche Position haben

def window_not_bigger_than_wall(window_len, window_width, wall_len, wall_width):
    if wall_len > window_len and wall_width > window_width:
        return True