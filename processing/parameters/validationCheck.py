from GUI import gui


# {"window_name": "Window0", "window_type": "Double Hung", "floor_win": "Floor0", "window_height": 2.0, "window_width": 2.0, "wind_dist_left": null, "wind_dist_up": null, "side": "front"}
# {"door_name": door_name, "side_width": door_width_wall, "width": door_width, "height": door_height, "door_type": door_type}
# {"House": {"Floor0": {"floor_name": "Floor0", "floor_height": 10.0, "floor_width": 10.0, "deleted": false, "Windows": {"w": {"window_name": "w", "window_type": "Double Hung", "floor_win": "Floor0", "window_height": 2.0, "window_width": 2.0, "side": "front"}}, "Doors": {"d": {"door_name": "d", "side_width": 5.0, "width": 2.0, "height": 10.0, "door_type": "Normal Door", "side": "front"}}, "height": 10.0}, "Floor1": {"floor_name": "Floor1", "floor_height": 10.0, "floor_width": 10.0, "deleted": false, "Windows": {}, "Doors": {}, "height": 20.0}, "Roof": {"roof_type": "Triangular Roof", "roof_height": 10.0, "roof_width": 10.0, "roof_name": "r"}}}

def object_collision(parameter, side):
    liste = gui.house_list
    # p1, p2
    for i in parameter:
        if parameter[i] == "door_name":
            for window_name in liste["House"]["Floor0"]["Windows"]:
            # liste["House"]["Floor0"]["Windows"][window_name]['p1']
            # do_overlap(p1,p2, s1,s2)
                if liste["House"]["Floor0"]["Windows"][window_name]["side"] == side:
                    p1 = parameter["House"]["Floor0"]["Windows"][window_name]['p1']
                    p2 = parameter["House"]["Floor0"]["Windows"][window_name]['p3']
                    s1 = (parameter["side_width"], 0)
                    s2 = (parameter["side_width"]+parameter["width"], parameter["height"])
                    if do_overlap(p1, p2, s1, s2):
                        print("ERROR")
                    else:
                        print("Fine")

        elif parameter[i] == 'window_name':
            for floor in liste["House"]:
                for window_name in liste["House"][floor]["Windows"]:
                    try:
                        if liste["House"]["Floor0"]["Windows"][window_name]["side"] == side:
                            p1 = parameter["House"]["Floor0"]["Windows"][window_name]['p1']
                            p2 = parameter["House"]["Floor0"]["Windows"][window_name]['p3']
                            s1 = (parameter["side_width"], 0)
                            s2 = (parameter["side_width"] + parameter["width"], parameter["height"])
                            if do_overlap(p1, p2, s1, s2):
                                print("ERROR")
                                return False
                            else:
                                print("Fine")
                                return True
                    except:
                        return False
                for door_name in liste["House"][floor]["Doors"]:
                    try:
                        if liste["House"]["Floor0"]["Doors"][door_name]["side"] == side:
                            p1 = parameter["House"]["Floor0"]["Windows"][window_name]['p1']
                            p2 = parameter["House"]["Floor0"]["Windows"][window_name]['p3']
                            s1 = (parameter["side_width"], 0)
                            s2 = (parameter["side_width"] + parameter["width"], parameter["height"])
                            if do_overlap(p1, p2, s1, s2):
                                print("ERROR")
                                return False
                            else:
                                print("Fine")
                                return True
                    except:
                        return False


# check overlapping rectangles
def do_overlap(p1, p2, s1, s2):
    for i in range(p1[0], p2[0], 0.001):
        for j in range(p1[1], p2[1], 0.001):
            pv = (i,j)
            # if rectangle has area 0, no overlap
            if pv == s1 or pv == s2:
                return True

            # If one rectangle is on left side of other
            # if p1[0] > s2[0] or s1[0] > p2[0]:
            #     return False

            # If one rectangle is above other
            # if p2[1] > s1[1] or s2[1] > p1[1]:
            #     return False

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
