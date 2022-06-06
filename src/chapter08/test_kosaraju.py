from unittest import TestCase

from chapter08.kosaraju import kosaraju, topo_sort


class Test(TestCase):
    def test_problem8_test1(self):
        file1 = open('../data/chapter08/problem8.10test1.txt', 'r')
        Lines = file1.readlines()

        g = {}
        for line in Lines:
            line = line.strip()
            v, w = line.split()
            v = int(v)
            w = int(w)
            if v not in g:
                g[v] = []
            g[v].append(w)
        sccs = kosaraju(g)
        # Top 5 SCC sizes: 3,3,3,0,0
        sccs.sort(key=len, reverse=True)
        i = 0
        top_5_scc_sizes = [3, 3, 3, 0, 0]
        for scc_size in top_5_scc_sizes:
            self.assertEqual(len(sccs[i]), scc_size)
            i += 1


    def test_topo_sort(self):
        g = {1: [2, 3], 2: [4], 3: [4], 4: []}
        result = topo_sort(g)
        self.assertEqual([1, 2, 3, 4], result)


    def test_topo_sort_rev(self):
        g = {1: [2, 3], 2: [4], 3: [4], 4: []}
        result = topo_sort(g, rev=True)
        self.assertEqual([4, 3, 2, 1], result)
