from GUI import gui, nodetree


def draw_floor(len, width, i):
    house_list = gui.house_list
    if i > 0:
        paras = house_list["House"]["Floor" + str(i - 1)]
        house_list["House"]["Floor" + str(i)]["height"] = width + paras["height"]
        heights = house_list["House"]["Floor" + str(i)]["height"]
        gui.dpg.draw_quad((0, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]), (0, heights),
                      (len, heights), (len, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]),
                      parent="plot", thickness=0.001)
    else:
        gui.dpg.draw_quad((0, 0), (0, width), (len, width), (len, 0), parent="plot", thickness=0.001)
        house_list["House"]["Floor0"]["height"] = width


def append_floor(liste):
    house_list = gui.house_list
    i = len(house_list["House"])
    house_list["House"]["Floor" + str(i)] = liste
    gui.draw.draw_floor(liste["floor_len"], liste["floor_width"], i)
    nodetree.nodes()

def draw_window(liste):
    house_list = gui.house_list
    for i in house_list["House"]:
        for j in house_list["House"][i]:
            if house_list["House"][i][j] == liste["floor_win"]:
                house_list["House"][i]["Windows"][liste["window_name"]] = liste
                wmiddle = house_list["House"][i]["floor_len"] / 2
                wlen = liste["window_len"] / 2
                wwidth = liste["window_width"] / 2
                if i != "Floor0":
                    middle = house_list["House"][i]["height"] - house_list["House"][i]["floor_width"] / 2
                    gui.dpg.draw_quad((wmiddle - wwidth, middle - wlen), (wmiddle + wwidth, middle - wlen),
                                  (wmiddle + wwidth, middle + wlen), (wmiddle - wwidth, middle + wlen),
                                  parent="plot",
                                  thickness=0.001)
                else:
                    middle = house_list["House"][i]["height"] / 2
                    gui.dpg.draw_quad((wmiddle - wwidth, middle - wlen), (wmiddle + wwidth, middle - wlen),
                                  (wmiddle + wwidth, middle + wlen), (wmiddle - wwidth, middle + wlen),
                                  parent="plot",
                                  thickness=0.001)
    nodetree.nodes()