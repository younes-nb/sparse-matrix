from View import View
from Model import Model


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()
        self.initButtons()

    def initButtons(self):
        self.view.firstMatrixTab.showButton.clicked.connect(self.initFirstShowButton)
        self.view.secondMatrixTab.showButton.clicked.connect(self.initSecondShowButton)

    def initFirstShowButton(self):
        self.view.firstMatrixTab.creatTable(
            int(self.view.firstMatrixTab.matrixRow.value()), int(self.view.firstMatrixTab.matrixColumn.value()),
            self.view.firstMatrixTab.matrix)

    def initSecondShowButton(self):
        self.view.secondMatrixTab.creatTable(
            int(self.view.secondMatrixTab.matrixRow.value()), int(self.view.secondMatrixTab.matrixColumn.value()),
            self.view.secondMatrixTab.matrix)
