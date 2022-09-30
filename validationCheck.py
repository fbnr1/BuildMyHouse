import GUI.gui


def constructbuilding():
    a = buildingconstructable()
    if a:
        pass  # code zum konstruieren des Gebäudes


def buildingconstructable():
    a = windowsvalid()
    b = widthandheightvalid()
    c = collision()
    d = roofheightnothigherthanbuildingheight()
    return a and b and c and d


def windowsvalid(windows, buildingheight, buildinglength):
    if (buildingheight * buildinglength) >= windows:
        return True


def widthandheightvalid(buildingheight, buildingwidth):
    if buildingheight != 0 and buildingwidth != 0:
        return True


def roofheightnothigherthanbuildingheight(buildingheight, roofheight):
    if buildingheight > roofheight:
        return True


def collision(object1, object2):
    pass  # if object1.pos != object2.pos --> return True, 2 Objekte sollen nicht die gleiche Position haben
