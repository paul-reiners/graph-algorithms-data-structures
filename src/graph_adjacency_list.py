class Graph_Adjacency_List(object):
  def __init__(self, vertices, incident_edges):
    self.vertices = sorted(vertices)
    self.incident_edges = sorted(incident_edges)
    self.explored = dict([v, False] for v in self.vertices)

  def mark_explored(self, v):
    self.explored[v] = True
