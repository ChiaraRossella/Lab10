import flet as ft
from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the modello, which implements the logic of the program and holds the data
        self._model = model




    def handleCalcola(self, e):
        anno= self._view._txtAnno.value
        if anno== "":
            self._view.create_alert("Inserire un anno compreso tra 1816 e 2016")
        else:
            try:
                anno = int(anno)
            except ValueError:
                self._view.create_alert("Inserire un anno compreso tra 1816 e 2016")
            if 1816<=anno<=2016:
                self._model.buildGraph(anno)
            else:
                self._view.create_alert("Inserire un anno compreso tra 1816 e 2016")





