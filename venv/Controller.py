from View import View
from Model import Model
from PyQt6.QtWidgets import QTableWidget


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()
        self.initButtons()

    def initButtons(self):
        self.view.firstMatrixTab.showButton.clicked.connect(self.initFirstShowButton)
        self.view.secondMatrixTab.showButton.clicked.connect(self.initSecondShowButton)
        self.view.firstMatrixTab.transposeButton.clicked.connect(self.initFirstTransposeButton)
        self.view.secondMatrixTab.transposeButton.clicked.connect(self.initSecondTransposeButton)

    def initFirstShowButton(self):
        self.view.firstMatrixTab.creatTable(
            int(self.view.firstMatrixTab.matrixRow.value()), int(self.view.firstMatrixTab.matrixColumn.value()),
            self.view.firstMatrixTab.matrix)
        self.view.firstMatrixTab.transposeButton.show()

    def initSecondShowButton(self):
        self.view.secondMatrixTab.creatTable(
            int(self.view.secondMatrixTab.matrixRow.value()), int(self.view.secondMatrixTab.matrixColumn.value()),
            self.view.secondMatrixTab.matrix)
        self.view.secondMatrixTab.transposeButton.show()

    def initFirstTransposeButton(self):
        sparse = self.convertToSparse(self.view.firstMatrixTab.matrix)
        transposedSparse = self.model.transpose(sparse)
        self.view.firstMatrixTab.creatTable(self.view.firstMatrixTab.matrix.columnCount(),
                                            self.view.firstMatrixTab.matrix.rowCount(),
                                            self.view.firstMatrixTab.matrix, transposedSparse)

    def initSecondTransposeButton(self):
        sparse = self.convertToSparse(self.view.secondMatrixTab.matrix)
        transposedSparse = self.model.transpose(sparse)
        self.view.secondMatrixTab.creatTable(self.view.secondMatrixTab.matrix.columnCount(),
                                             self.view.secondMatrixTab.matrix.rowCount(),
                                             self.view.secondMatrixTab.matrix, transposedSparse)

    def convertToSparse(self, matrix=QTableWidget):
        sparse = []
        for i in range(matrix.rowCount()):
            for j in range(matrix.columnCount()):
                if (matrix.item(i, j).text() != '0'):
                    sparse.append((i, j, float(matrix.item(i, j).text())))

        return sparse
