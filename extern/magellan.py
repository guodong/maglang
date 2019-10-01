def export(name, func):
    pass


topo = {}


class PathElement:
    def __init__(self, src, dst):
        self.mode = 0
        self.src = src
        self.dst = dst


def to_magellan_path(path):
    result = []
    for i in range(0, len(path), 2):
        result.append(PathElement(path[i], path[i + 1]))

    return result


helper = {

}


def assign_label(func):
    pass


topology = {}


def peer(swport):
    link = [link for link in topo.links if swport in link]
    link[0].remove(swport)
    return link[0][0]
