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
    save_path = 'save'
    name = os.path.join(save_path, filename)
    newfile = codecs.open(name, "r+", encoding="utf8", errors="ignore")
    liste = {}
    for i in newfile:
        liste = json.loads(i)
    GUI.gui.house_list = liste
    for floor in liste['House']:
        if floor != "Roof":
            print(print(liste['House'][floor]))
            draw.append_floor(liste['House'][floor], liste)
            for window in liste['House'][floor]['Windows']:
                print(liste['House'][floor]['Windows'])
                draw.draw_window(liste['House'][floor]['Windows'][window], liste)
    return liste
