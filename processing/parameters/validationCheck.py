from GUI import gui


def object_collision(parameter, side):
    liste = gui.house_list
    for i in parameter:
        if i == "door_name":
            for window_name in liste["House"]["Floor0"]["Windows"]:
                if liste["House"]["Floor0"]["Windows"][window_name]["side"] == side:
                    p1 = liste["House"]["Floor0"]["Windows"][window_name]['p1']
                    p2 = liste["House"]["Floor0"]["Windows"][window_name]['p3']
                    s1 = (parameter["side_width"], 0)
                    s2 = (parameter["side_width"]+parameter["width"], parameter["height"])
                    if do_overlap(p1, p2, s1, s2):
                        return True
        elif i == 'window_name':
            for floor in liste["House"]:
                for window_name in liste["House"][floor]["Windows"]:
                    if liste["House"]["Floor0"]["Windows"][window_name]["side"] == side:
                        p1 = liste["House"][floor]["Windows"][window_name]['p1']
                        p2 = liste["House"][floor]["Windows"][window_name]['p3']
                        s1 = parameter["p1"]
                        s2 = parameter["p3"]
                        if do_overlap(p1, p2, s1, s2):
                            return True
                for door_name in liste["House"][floor]["Doors"]:
                    if liste["House"]["Floor0"]["Doors"][door_name]["side"] == side:
                        p1 = (liste["House"]["Floor0"]["Doors"][door_name]["side_width"], 0)
                        p2 = (liste["House"]["Floor0"]["Doors"][door_name]["side_width"] + liste["House"]["Floor0"][
                            "Doors"][door_name]["side_width"], liste["House"]["Floor0"]["Doors"][door_name]["height"])
                        s1 = parameter["p1"]
                        s2 = parameter["p3"]
                        if do_overlap(p1, p2, s1, s2):
                            return True
    return False


# check overlapping rectangles
def do_overlap(p1, p2, s1, s2):

    if p1[0] < s1[0] < p2[0] and p1[1] < s2[1] < p2[1]:
        return True
    elif p1[0] < s1[0] < p2[0] and p1[1] < s1[1] < p2[1]:
        return True
    elif p1[0] < s2[0] < p2[0] and p1[1] < s1[1] < p2[1]:
        return True
    elif p1[0] < s2[0] < p2[0] and p1[1] < s2[1] < p2[1]:
        return True

    return False


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
