from GUI import gui


# def construct_building():
#     a = building_constructable()
#     if a:
#         pass  # code zum konstruieren des Gebäudes
#
#
# def building_constructable():
#
#     a = width_and_height_valid()
#     b = roof_height_not_higher_than_building_height()
#     return a and b
#
#
# def width_and_height_valid(wall_len, wall_width):
#     if wall_width != 0 and wall_len != 0:
#         return True
#
#
# def roof_height_not_higher_than_building_height(wall_width, roofheight):
#     if wall_width > roofheight:
#         return True

# {"window_name": "Window0", "window_type": "Double Hung", "floor_win": "Floor0", "window_height": 2.0, "window_width": 2.0, "wind_dist_left": null, "wind_dist_up": null, "side": "front"}
# {"door_name": door_name, "side_width": door_width_wall, "width": door_width, "height": door_height, "door_type": door_type}
# {"House": {"Floor0": {"floor_name": "Floor0", "floor_height": 10.0, "floor_width": 10.0, "deleted": false, "Windows": {"w": {"window_name": "w", "window_type": "Double Hung", "floor_win": "Floor0", "window_height": 2.0, "window_width": 2.0, "side": "front"}}, "Doors": {"d": {"door_name": "d", "side_width": 5.0, "width": 2.0, "height": 10.0, "door_type": "Normal Door", "side": "front"}}, "height": 10.0}, "Floor1": {"floor_name": "Floor1", "floor_height": 10.0, "floor_width": 10.0, "deleted": false, "Windows": {}, "Doors": {}, "height": 20.0}, "Roof": {"roof_type": "Triangular Roof", "roof_height": 10.0, "roof_width": 10.0, "roof_name": "r"}}}

def object_collision(parameter, side):
    liste = gui.house_list
    #p1, p2

    if parameter['door_name']:
        for window_name in liste["House"]["Floor0"]["Windows"]:
            # liste["House"]["Floor0"]["Windows"][window_name]['p1']
            #do_overlap(p1,p2, s1,s2)
            if liste["House"]["Floor0"]["Windows"][window_name]["side"] == side:
                pass
    elif parameter['window_name']:
        for i in liste["House"]:
            if i != "Roof":
                for j in liste["House"][i]:
                    pass


# check overlapping rectangles
def do_overlap(p1, p2, s1, s2):
    # if rectangle has area 0, no overlap
    if p1[0] == p2[0] or p1[1] == p2[1] or s2[0] == s1[0] or s1[1] == s2[1]:
        return False

    # If one rectangle is on left side of other
    if p1[0] > s2[0] or s1[0] > p2[0]:
        return False

    # If one rectangle is above other
    if p2[1] > s1[1] or s2[1] > p1[1]:
        return False

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
        if i != "Roof":
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
