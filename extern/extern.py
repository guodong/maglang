from magellan import export, topo, helper, assign_label, topology
import networkx

@assign_label
def assign(port):
    if isinstance(port.peer().device, topology.Host):
        return 'external_ingress'

def shortest_path(src, dst):
    G = networkx.Graph()
    G.add_edges(topo.links)
    path = networkx.shortest_path(G)
    return helper.to_magellan_path(path)


def peer(swport):
    link = [link for link in topo.links if swport in link]
    link[0].remove(swport)
    return link[0][0]


export('shortest_path', shortest_path)
export('peer', peer)
