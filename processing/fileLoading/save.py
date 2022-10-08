import codecs
import json
import os.path

import GUI.gui
from GUI.drawing import draw


def save(lists, filename):
    print(lists)
    save_path = 'save'
    name = os.path.join(save_path, filename)
    name = name + '.jsonl'
    newfile = codecs.open(name, "w+", encoding="utf8", errors="ignore")
    newfile.write(json.dumps(lists))


def load(filename):
    print("loading...")
    floor_num = -1
    save_path = 'save'
    name = os.path.join(save_path, filename)
    newfile = codecs.open(name, "r+", encoding="utf8", errors="ignore")
    liste = {}
    for i in newfile:
        liste = json.loads(i)
    GUI.gui.house_list = liste
    for floor in liste['House']:
        if floor != "Roof":
            floor_num += 1
            print(print(liste['House'][floor]))
            draw.draw_floor(liste['House'][floor]["floor_height"], liste['House'][floor]["floor_width"], floor_num, liste)
            for window in liste['House'][floor]['Windows']:
                print(liste['House'][floor]['Windows'])
                draw.draw_window(liste['House'][floor]['Windows'][window], liste)
    return liste
