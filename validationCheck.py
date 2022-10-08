from GUI import gui


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
    if window_count <= 0 or window_count == 1:
        return True
    if window_count > 1:
        if window_count <= (wall_len - 2) + ((window_count - 1) * 0.5):   #links und rechts an den Ecken der Wand jeweils 1 Meter frei
            return True                                                   # zwischen den Fenstern mindestens 0.5 m Platz



def width_and_height_valid(wall_len, wall_width):
    if wall_width != 0 and wall_len != 0:
        return True


def roofheight_not_higher_than_buildingheight(wall_width, roofheight):
    if wall_width > roofheight:
        return True


def collision(object1, object2):
    pass  # if object1.pos != object2.pos --> return True, 2 Objekte sollen nicht die gleiche Position haben

def window_not_bigger_than_wall(window_width, window_len, wall_len, wall_width):
    if wall_len > window_len and wall_width > window_len:
        return True


def name_collision_floor(name):
    house_list = gui.house_list
    for i in house_list["House"]:
        for j in house_list["House"][i]["floor_name"]:
            if name == j:
                return False
    return True
