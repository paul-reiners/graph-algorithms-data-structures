cur_label = None
num_scc = 0
scc = dict()


def dfs_topo(g, s, explored, f, rev=False):
    # Input: graph G = (V, E) in adjacency-list representation, and a vertex s in V.
    # Postcondition: every vertex reachable from s is marked as "explored" and has an assigned f-value.
    explored[s - 1] = True
    global cur_label
    for v in g[s]:
        if not explored[v - 1]:
            dfs_topo(g, v, explored, f, rev)
    if rev:
        f.append(cur_label)
    else:
        f.insert(0, cur_label)
    cur_label -= 1


def topo_sort(g, rev=False):
    # Input: directed acyclic graph G = (V, E) in adjacency-list representation.
    # Postondition: the f-values of vertices constitute a topological ordering of G
    explored = [False] * len(g)
    global cur_label
    cur_label = len(g)  # keeps track of ordering
    f = []
    for v in g:
        if not explored[v - 1]:  # in a prior DFS
            dfs_topo(g, v, explored, f, rev)
    return f


def dfs_scc(g, s):
    """The same as DFS, with one additional line of bookkeeping.

         :param g: directed graph G = (V, E) in adjacency-list representation
         :param s: vertex s ∈ V
         :postcondition: every vertex reachable from s is marked as "explored" and has an assigned scc-value.
    """
    g.mark_explored(s)
    global scc
    scc[s] = num_scc  # global variable above
    s_edges = g.get_edges(s)
    for v in s_edges:
        if not g.explored(v):
            dfs_scc(g, v)


def kosaraju(g):
    # Input: directed graph G = (V, E) in adjacency -list representation, with V = {1, 2, 3, ..., n}.
    # Postcondition: for every v, w in V, scc(v) = scc(2) if and only if v, w are in same SCC of G.
    global scc
    [False] * len(g)
    # first pass of depth-first search
    # (computes f(v)'s, the magical ordering)
    f = topo_sort(g, rev=True)

    # seond pass of depth-first search
    # (finds SCCs in reverse topological order)
    g_vertices = list(g.keys())
    explored = dict([(v, False) for v in g_vertices])
    global num_scc
    num_scc = 0
    for v in f:
        if not explored[v]:
            num_scc += 1
            # assign scc-values
            dfs_scc(g, v)
