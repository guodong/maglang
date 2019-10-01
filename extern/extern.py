from magellan import export, topo, helper, assign_label, topology
import networkx


@assign_label
def assign(port):
    if isinstance(port.peer().device, topology.Host):
        return 'external_ingress'


def shortest_path(src, dst):
    G = networkx.Graph()
    G.add_edges(topo.links)
    path = networkx.shortest_path(G, src, dst)
    return helper.to_magellan_path(path)


def stp_path(root):
    G = networkx.Graph()
    G.add_edges(topo.links)
    stp = networkx.minimal_spanning_tree(G, root)
    return helper.to_magellan_path(stp)


export('shortest_path', shortest_path)
export('stp_path', stp_path)
