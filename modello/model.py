import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._idMap = {}
        self._edges = None
        self._nodes = None
        self._grafo = nx.Graph()

    def buildGraph(self, anno:int):
        self._grafo.clear()
        self.fillIDMap()
        self._edges=




    def fillIDMap(self):
        for n in DAO.getAllCountries():
            self._idMap[n.CCode] = n
