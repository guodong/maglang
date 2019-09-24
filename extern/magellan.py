def export(name, func):
    pass

topo = {}

helper = {}

def assign_label():
    pass

topology = {}


def peer(swport):
    link = [link for link in topo.links if swport in link]
    link[0].remove(swport)
    return link[0][0]