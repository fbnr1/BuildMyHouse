from GUI import gui, nodetree

global layer
layer = {"layers": {"front": [], "right": [], "left": [], "back": []}}
global side
side = "front"


def draw_floor(len, width, i):
    global layer
    global side
    house_list = gui.house_list
    if i > 0:
        paras = house_list["House"]["Floor" + str(i - 1)]
        house_list["House"]["Floor" + str(i)]["height"] = width + paras["height"]
        heights = house_list["House"]["Floor" + str(i)]["height"]
        gui.dpg.draw_quad((0, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]), (0, heights),
                          (len, heights), (len, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]),
                          parent="plot", thickness=0.001)
    else:
        gui.dpg.draw_quad((0, 0), (0, width), (len, width), (len, 0), parent="plot", thickness=0.001,
                          tag=house_list["House"]["Floor0"]["floor_name"]+"f", show=False)
        layer["layers"]["front"].append(house_list["House"]["Floor0"]["floor_name"]+"f")

        gui.dpg.draw_quad((0, 0), (0, width), (len, width), (len, 0), parent="plot", thickness=0.001,
                          tag=house_list["House"]["Floor0"]["floor_name"] + "l", show=False)
        layer["layers"]["left"].append(house_list["House"]["Floor0"]["floor_name"] + "l")

        gui.dpg.draw_quad((0, 0), (0, width), (len, width), (len, 0), parent="plot", thickness=0.001,
                          tag=house_list["House"]["Floor0"]["floor_name"] + "r", show=False)
        layer["layers"]["right"].append(house_list["House"]["Floor0"]["floor_name"] + "r")

        gui.dpg.draw_quad((0, 0), (0, width), (len, width), (len, 0), parent="plot", thickness=0.001,
                          tag=house_list["House"]["Floor0"]["floor_name"] + "b", show=False)
        layer["layers"]["back"].append(house_list["House"]["Floor0"]["floor_name"] + "b")

        switch_layer()

        house_list["House"]["Floor0"]["height"] = width


def append_floor(liste):
    print(liste)
    house_list = gui.house_list
    i = len(house_list["House"])
    print(i)
    house_list["House"]["Floor" + str(i)] = liste
    draw_floor(liste["floor_len"], liste["floor_width"], i)
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


def switch_layer():
    global layer
    global side
    print(side)
    if side == "front":
        for i in layer["layers"]["front"]:
            gui.dpg.show_item(item=i)
        for i in layer["layers"]["right"]:
            gui.dpg.hide_item(item=i)
        for i in layer["layers"]["left"]:
            gui.dpg.hide_item(item=i)
        for i in layer["layers"]["back"]:
            gui.dpg.hide_item(item=i)
    elif side == "right":
        for i in layer["layers"]["front"]:
            gui.dpg.hide_item(item=i)
        for i in layer["layers"]["right"]:
            gui.dpg.show_item(item=i)
        for i in layer["layers"]["left"]:
            gui.dpg.hide_item(item=i)
        for i in layer["layers"]["back"]:
            gui.dpg.hide_item(item=i)
    elif side == "left":
        for i in layer["layers"]["front"]:
            gui.dpg.hide_item(item=i)
        for i in layer["layers"]["right"]:
            gui.dpg.hide_item(item=i)
        for i in layer["layers"]["left"]:
            gui.dpg.show_item(item=i)
        for i in layer["layers"]["back"]:
            gui.dpg.hide_item(item=i)
    elif side == "back":
        for i in layer["layers"]["front"]:
            gui.dpg.hide_item(item=i)
        for i in layer["layers"]["right"]:
            gui.dpg.hide_item(item=i)
        for i in layer["layers"]["left"]:
            gui.dpg.hide_item(item=i)
        for i in layer["layers"]["back"]:
            gui.dpg.show_item(item=i)


def switch_side(s):
    global side
    side = s
    switch_layer()
