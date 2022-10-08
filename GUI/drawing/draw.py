from processing.parameters import validationCheck
from GUI import gui, nodetree

global layer
layer = {"layers": {"front": [], "right": [], "left": [], "back": []}}
global side
side = "front"

def draw_floor(len, width, i, house_list):
    global layer
    global side
    if i > 0:
        paras = house_list["House"]["Floor" + str(i - 1)]
        gui.house_list["House"]["Floor" + str(i)]["height"] = width + paras["height"]
        heights = house_list["House"]["Floor" + str(i)]["height"]

        gui.dpg.draw_quad((0, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]), (0, heights),
                          (len, heights), (len, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]),
                          parent="plot", thickness=0.001, tag=house_list["House"]["Floor" + str(i)]["floor_name"] + "f",
                          show=False)
        layer["layers"]["front"].append(house_list["House"]["Floor" + str(i)]["floor_name"] + "f")

        gui.dpg.draw_quad((0, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]), (0, heights),
                          (len, heights), (len, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]),
                          parent="plot", thickness=0.001, tag=house_list["House"]["Floor" + str(i)]["floor_name"] + "l",
                          show=False)
        layer["layers"]["left"].append(house_list["House"]["Floor" + str(i)]["floor_name"] + "l")

        gui.dpg.draw_quad((0, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]), (0, heights),
                          (len, heights), (len, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]),
                          parent="plot", thickness=0.001, tag=house_list["House"]["Floor" + str(i)]["floor_name"] + "r",
                          show=False)
        layer["layers"]["right"].append(house_list["House"]["Floor" + str(i)]["floor_name"] + "r")

        gui.dpg.draw_quad((0, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]), (0, heights),
                          (len, heights), (len, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]),
                          parent="plot", thickness=0.001, tag=house_list["House"]["Floor" + str(i)]["floor_name"] + "b",
                          show=False)
        layer["layers"]["back"].append(house_list["House"]["Floor" + str(i)]["floor_name"] + "b")

        switch_layer()
    else:
        gui.dpg.draw_quad((0, 0), (0, width), (len, width), (len, 0), parent="plot", thickness=0.001,
                          tag=house_list["House"]["Floor0"]["floor_name"] + "f", show=False)
        layer["layers"]["front"].append(house_list["House"]["Floor0"]["floor_name"] + "f")

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

        gui.house_list["House"]["Floor0"]["height"] = width



        a = validationCheck.width_and_height_valid(len, width)
        """""
        gui.dpg.create_context()
        with gui.dpg.window(label="Test"):
            gui.dpg.add_text(a)
        """

def append_floor(liste, house_list):
    i = len(house_list["House"])
    if liste["floor_name"] == "":
        liste["floor_name"] = "Floor" + str(i)
    gui.house_list["House"]["Floor" + str(i)] = liste
    draw_floor(liste["floor_height"], liste["floor_width"], i, gui.house_list)
    nodetree.nodes()


def draw_window(liste, house_list, seite=side):
    for i in house_list["House"]:
        for j in house_list["House"][i]:
            if house_list["House"][i][j] == liste["floor_win"]:
                gui.house_list["House"][i]["Windows"][liste["window_name"]] = liste
                gui.house_list["House"][i]["Windows"][liste["window_name"]]["side"] = seite
                wmiddle = house_list["House"][i]["floor_height"] / 2
                wlen = liste["window_height"] / 2
                wwidth = liste["window_width"] / 2
                if i != "Floor0":
                    middle = house_list["House"][i]["height"] - house_list["House"][i]["floor_width"] / 2
                    gui.dpg.draw_quad((wmiddle - wwidth, middle - wlen), (wmiddle + wwidth, middle - wlen),
                                      (wmiddle + wwidth, middle + wlen), (wmiddle - wwidth, middle + wlen),
                                      parent="plot", thickness=0.001, tag=liste["window_name"] + "w", show=False)

                else:
                    middle = house_list["House"][i]["height"] / 2
                    gui.dpg.draw_quad((wmiddle - wwidth, middle - wlen), (wmiddle + wwidth, middle - wlen),
                                      (wmiddle + wwidth, middle + wlen), (wmiddle - wwidth, middle + wlen),
                                      parent="plot", thickness=0.001, tag=liste["window_name"] + "w", show=False)

                if house_list["House"][i]["Windows"][liste["window_name"]]["side"] == "front":
                    layer["layers"]["front"].append(liste["window_name"] + "w")
                elif house_list["House"][i]["Windows"][liste["window_name"]]["side"] == "back":
                    layer["layers"]["back"].append(liste["window_name"] + "w")
                elif house_list["House"][i]["Windows"][liste["window_name"]]["side"] == "right":
                    layer["layers"]["right"].append(liste["window_name"] + "w")
                elif house_list["House"][i]["Windows"][liste["window_name"]]["side"] == "left":
                    layer["layers"]["left"].append(liste["window_name"] + "w")

    switch_layer()
    nodetree.nodes()


def switch_layer():
    global layer
    global side
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


def draw_door(liste, seite=side):
    paras = liste["Door"]
    if paras["door_type"] != "Normal Door":
        gui.dpg.draw_line((paras["side_width"]+paras["width"]/2,0),(paras["side_width"]+paras["width"]/2,paras["height"]), tag=paras["door_name"] + "ld", parent="plot", thickness=0.001, show=False)
    gui.dpg.draw_quad((paras["side_width"], 0), (paras["side_width"], paras["height"]), (paras["side_width"] +
                                                                                         paras["width"],
                                                                                         paras["height"]),
                      (paras["side_width"] + paras["width"], 0),
                      tag=paras["door_name"] + "d", parent="plot", thickness=0.001, show=False)
    gui.house_list["House"]["Floor0"]["Doors"][liste["Door"]["door_name"]] = paras
    gui.house_list["House"]["Floor0"]["Doors"][liste["Door"]["door_name"]]["side"] = seite
    if gui.house_list["House"]["Floor0"]["Doors"][liste["Door"]["door_name"]]["side"] == "front":
        layer["layers"]["front"].append(paras["door_name"] + "d")
        if paras["door_type"] != "Normal Door":
            layer["layers"]["front"].append(paras["door_name"] + "ld")
    elif gui.house_list["House"]["Floor0"]["Doors"][liste["Door"]["door_name"]]["side"] == "back":
        layer["layers"]["back"].append(paras["door_name"] + "d")
        if paras["door_type"] != "Normal Door":
            layer["layers"]["front"].append(paras["door_name"] + "ld")
    elif gui.house_list["House"]["Floor0"]["Doors"][liste["Door"]["door_name"]]["side"] == "right":
        layer["layers"]["right"].append(paras["door_name"] + "d")
        if paras["door_type"] != "Normal Door":
            layer["layers"]["front"].append(paras["door_name"] + "ld")
    elif gui.house_list["House"]["Floor0"]["Doors"][liste["Door"]["door_name"]]["side"] == "left":
        layer["layers"]["left"].append(paras["door_name"] + "d")
        if paras["door_type"] != "Normal Door":
            layer["layers"]["front"].append(paras["door_name"] + "ld")
    switch_layer()
    nodetree.nodes()


def draw_roof(liste, l, house_list):
    floor = "Floor" + str(l)
    height = house_list["House"][floor]["height"]
    width = house_list["House"][floor]["floor_width"]
    r_width = liste["roof_width"]
    r_height = liste["roof_height"]
    if not width - r_width > 0:
        if liste["roof_type"] == "Triangular Roof":
            if width - r_width < 0:
                gui.dpg.draw_triangle(((width-r_width)/2, height), (width / 2, r_height + height), (((width-r_width)/2)*-1+width,
                                                                                                    height), parent="plot", thickness=0.001)
            else:
                gui.dpg.draw_triangle((0,height),(width/2,r_height+height),(width,height), parent="plot", thickness=0.001)
        else:
            gui.dpg.draw_quad((0,height),(0,height+r_height),(width,height+r_height),(width,height), parent="plot", thickness=0.001)
        switch_layer()
        gui.house_list["House"]["Roof"] = liste
        gui.house_list["House"]["Roof"]["roof_width"] = width
        nodetree.nodes()
    else:
        print("ERRORORORR")
