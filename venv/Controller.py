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
        self.view.resultMatrixTab.sumButton.clicked.connect(self.initSumButton)

    def initFirstShowButton(self):
        self.view.firstMatrixTab.errorLabel.hide()
        self.view.firstMatrixTab.creatTable(
            int(self.view.firstMatrixTab.matrixRow.value()), int(self.view.firstMatrixTab.matrixColumn.value()),
            self.view.firstMatrixTab.matrix)
        self.view.firstMatrixTab.transposeButton.show()

    def initSecondShowButton(self):
        self.view.secondMatrixTab.errorLabel.hide()
        self.view.secondMatrixTab.creatTable(
            int(self.view.secondMatrixTab.matrixRow.value()), int(self.view.secondMatrixTab.matrixColumn.value()),
            self.view.secondMatrixTab.matrix)
        self.view.secondMatrixTab.transposeButton.show()

    def initFirstTransposeButton(self):
        try:
            self.view.firstMatrixTab.errorLabel.hide()
            self.view.firstMatrixTab.matrixRow.setValue(self.view.firstMatrixTab.matrix.columnCount())
            self.view.firstMatrixTab.matrixColumn.setValue(self.view.firstMatrixTab.matrix.rowCount())
            sparse = self.convertToSparse(self.view.firstMatrixTab.matrix)
            if sparse == []:
                self.view.firstMatrixTab.creatTable(self.view.firstMatrixTab.matrix.columnCount(),
                                                    self.view.firstMatrixTab.matrix.rowCount(),
                                                    self.view.firstMatrixTab.matrix)
            else:
                transposedSparse = self.model.transpose(sparse)
                self.view.firstMatrixTab.creatTable(self.view.firstMatrixTab.matrix.columnCount(),
                                                    self.view.firstMatrixTab.matrix.rowCount(),
                                                    self.view.firstMatrixTab.matrix, transposedSparse)
        except:
            self.view.firstMatrixTab.errorLabel.show()

    def initSecondTransposeButton(self):
        try:
            self.view.secondMatrixTab.errorLabel.hide()
            self.view.secondMatrixTab.matrixRow.setValue(self.view.secondMatrixTab.matrix.columnCount())
            self.view.secondMatrixTab.matrixColumn.setValue(self.view.secondMatrixTab.matrix.rowCount())
            sparse = self.convertToSparse(self.view.secondMatrixTab.matrix)
            if sparse == []:
                self.view.secondMatrixTab.creatTable(self.view.secondMatrixTab.matrix.columnCount(),
                                                     self.view.secondMatrixTab.matrix.rowCount(),
                                                     self.view.secondMatrixTab.matrix)
            else:
                transposedSparse = self.model.transpose(sparse)
                self.view.secondMatrixTab.creatTable(self.view.secondMatrixTab.matrix.columnCount(),
                                                     self.view.secondMatrixTab.matrix.rowCount(),
                                                     self.view.secondMatrixTab.matrix, transposedSparse)
        except:
            self.view.secondMatrixTab.errorLabel.show()

    def initSumButton(self):
        try:
            self.view.resultMatrixTab.errorLabel.hide()
            if self.view.firstMatrixTab.matrix.rowCount() != self.view.secondMatrixTab.matrix.rowCount() or self.view.firstMatrixTab.matrix.columnCount() != self.view.secondMatrixTab.matrix.columnCount():
                raise Exception

            sum = self.model.sum(self.convertToSparse(self.view.firstMatrixTab.matrix),
                                 self.convertToSparse(self.view.secondMatrixTab.matrix))

            self.view.resultMatrixTab.creatTable(self.view.firstMatrixTab.matrix.rowCount(),
                                                 self.view.firstMatrixTab.matrix.columnCount(),
                                                 self.view.resultMatrixTab.matrix, sum)
        except:
            self.view.resultMatrixTab.errorLabel.show()

    def initSubButton(self):
        pass

    def initMulButton(self):
        pass

    def convertToSparse(self, matrix=QTableWidget):
        sparse = []
        for i in range(matrix.rowCount()):
            for j in range(matrix.columnCount()):
                if (matrix.item(i, j).text() != '0'):
                    sparse.append((i, j, float(matrix.item(i, j).text())))

        return sparse
