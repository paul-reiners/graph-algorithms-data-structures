cur_label = None
explored = {}
num_scc = None
scc = {}


def dfs_topo(g, s, f, rev=False):
    # Input: graph G = (V, E) in adjacency-list representation, and a vertex s in V.
    # Postcondition: every vertex reachable from s is marked as "explored" and has an assigned f-value.
    explored[s - 1] = True
    global cur_label
    for v in g[s]:
        if not explored[v - 1]:
            dfs_topo(g, v, f, rev)
    if rev:
        f.append(cur_label)
    else:
        f.insert(0, cur_label)
    cur_label -= 1


def topo_sort(g, max_node, rev=False):
    # Input: directed acyclic graph G = (V, E) in adjacency-list representation.
    # Postondition: the f-values of vertices constitute a topological ordering of G
    global explored
    explored = [False] * max_node
    global cur_label
    cur_label = len(g) + 1  # keeps track of ordering
    f = []
    for v in g:
        if not explored[v - 1]:  # in a prior DFS
            dfs_topo(g, v, f, rev)
    return f


def dfs_scc(g, s):
    # Input: directed graph G = (V, E) in adjacency-list representation, and a vertex s in V.
    # Postcondition: every vertex reachable from s is marked as "explored" and has an assigned scc-value.
    global explored
    explored[s - 1] = True
    global scc
    global num_scc
    scc[s] = num_scc
    if s - 1 in g:
        for v in g[s - 1]:
            if not explored[v - 1]:
                dfs_scc(g, v)


def kosaraju(g):
    # Input: directed graph G = (V, E) in adjacency -list representation, with V = {1, 2, 3, ..., n}.
    # Postcondition: for every v, w in V, scc(v) = scc(2) if and only if v, w are in same SCC of G.
    global explored
    explored = [False] * len(g)
    # first pass of depth-first search
    # (computes f(v)'s, the magical ordering)
    f = topo_sort(g, rev=True)

    # seond pass of depth-first search
    # (finds SCCs in reverse topological order)
    explored = [False] * len(g)
    global num_scc
    num_scc = 0
    for v in f:
        if not explored[v - 1]:
            num_scc += 1
            # assign scc-values
            dfs_scc(g, v)
    print('scc:', scc)
