from GUI import gui


def construct_building():
    a = building_constructable()
    if a:
        pass  # code zum konstruieren des Gebäudes


def building_constructable():

    a = width_and_height_valid()
    b = roof_height_not_higher_than_building_height()
    return a and b


def width_and_height_valid(wall_len, wall_width):
    if wall_width != 0 and wall_len != 0:
        return True


def roof_height_not_higher_than_building_height(wall_width, roofheight):
    if wall_width > roofheight:
        return True


def name_collision_floor(name):
    house_list = gui.house_list
    for i in house_list["House"]:
        if name == house_list["House"][i]["floor_name"]:
            return False
    return True


def name_collision_window(param):
    house_list = gui.house_list
    for i in house_list["House"]:
        for j in house_list["House"][i]["Windows"]:
            if param == j:
                return False
    return True


def name_collision_door(name):
    for i in gui.house_list["House"]["Floor0"]["Doors"]:
        print(i)
        if name == i:
            return False
    return True


def door_side(side):
    house_list = gui.house_list
    for i in house_list["House"]["Floor0"]["Doors"]:
        if house_list["House"]["Floor0"]["Doors"][i]["side"] == side:
            return False
    return True


def check_for_roof():
    for i in gui.house_list["House"]:
        if i == "Roof":
            return True
    return False
