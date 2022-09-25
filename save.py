import codecs
import json
import os.path


def save(lists, filename):
    print(lists)
    save_path = '.\saves'
    name = os.path.join(save_path, filename)
    name = name + '.jsonl'
    newfile = codecs.open(name, "w+", encoding="utf8", errors="ignore")
    newfile.write(json.dumps(lists))


def load(filename):
    save_path = '.\saves'
    name = os.path.join(save_path, filename)
    name = name + '.jsonl'
    newfile = codecs.open(name, "r+", encoding="utf8", errors="ignore")
    liste = {}
    for i in newfile:
        liste = json.loads(i)
    return liste

class Save(object):
    def __int__(self, name):
        self.name = name


'''if __name__ == '__main__':
    list = {'test': "test"}
    #save(list, "test")
    liste = load("test")
    print(liste)'''
