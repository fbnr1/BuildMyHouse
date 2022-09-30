import codecs
import json
import os.path

import GUI.gui


def save(lists, filename):
    print(lists)
    save_path = '.\save'
    name = os.path.join(save_path, filename)
    name = name + '.jsonl'
    newfile = codecs.open(name, "w+", encoding="utf8", errors="ignore")
    newfile.write(json.dumps(lists))


def load(filename):
    save_path = '.\save'
    name = os.path.join(save_path, filename)
    #name = name + '.jsonl'
    newfile = codecs.open(name, "r+", encoding="utf8", errors="ignore")
    liste = {}
    for i in newfile:
        liste = json.loads(i)
    for floor in liste['House']:
        GUI.gui.append_floor(liste['House'][floor])
    return liste
