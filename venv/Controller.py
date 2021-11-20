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
        self.view.resultMatrixTab.subButton.clicked.connect(self.initSubButton)
        self.view.resultMatrixTab.mulButton.clicked.connect(self.initMulButton)
        self.view.resultMatrixTab.sparseButton.clicked.connect(self.initSparseButton)

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

            self.view.firstMatrixTab.matrixRow.setValue(self.view.firstMatrixTab.matrix.columnCount())
            self.view.firstMatrixTab.matrixColumn.setValue(self.view.firstMatrixTab.matrix.rowCount())
        except:
            self.view.firstMatrixTab.errorLabel.show()

    def initSecondTransposeButton(self):
        try:
            self.view.secondMatrixTab.errorLabel.hide()
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

            self.view.secondMatrixTab.matrixRow.setValue(self.view.secondMatrixTab.matrix.columnCount())
            self.view.secondMatrixTab.matrixColumn.setValue(self.view.secondMatrixTab.matrix.rowCount())
        except:
            self.view.secondMatrixTab.errorLabel.show()

    def initSumButton(self):
        try:
            self.view.resultMatrixTab.errorLabel.hide()
            if self.view.firstMatrixTab.matrix.rowCount() != self.view.secondMatrixTab.matrix.rowCount() or self.view.firstMatrixTab.matrix.columnCount() != self.view.secondMatrixTab.matrix.columnCount():
                raise Exception

            sum = self.model.sum(self.convertToSparse(self.view.firstMatrixTab.matrix),
                                 self.convertToSparse(self.view.secondMatrixTab.matrix))
            self.view.resultMatrixTab.originRow = self.view.firstMatrixTab.matrix.rowCount()
            self.view.resultMatrixTab.originColumn = self.view.firstMatrixTab.matrix.columnCount()
            self.view.resultMatrixTab.creatTable(self.view.resultMatrixTab.originRow,
                                                 self.view.resultMatrixTab.originColumn,
                                                 self.view.resultMatrixTab.matrix, sum)

            self.view.resultMatrixTab.sparseButton.setEnabled(True)
        except:
            self.view.resultMatrixTab.errorLabel.show()

    def initSubButton(self):
        try:
            self.view.resultMatrixTab.errorLabel.hide()
            if self.view.firstMatrixTab.matrix.rowCount() != self.view.secondMatrixTab.matrix.rowCount() or self.view.firstMatrixTab.matrix.columnCount() != self.view.secondMatrixTab.matrix.columnCount():
                raise Exception

            subtract = self.model.subtract(self.convertToSparse(self.view.firstMatrixTab.matrix),
                                           self.convertToSparse(self.view.secondMatrixTab.matrix))

            self.view.resultMatrixTab.originRow = self.view.firstMatrixTab.matrix.rowCount()
            self.view.resultMatrixTab.originColumn = self.view.firstMatrixTab.matrix.columnCount()
            self.view.resultMatrixTab.creatTable(self.view.resultMatrixTab.originRow,
                                                 self.view.resultMatrixTab.originColumn,
                                                 self.view.resultMatrixTab.matrix, subtract)

            self.view.resultMatrixTab.sparseButton.setEnabled(True)
        except:
            self.view.resultMatrixTab.errorLabel.show()

    def initMulButton(self):
        try:
            self.view.resultMatrixTab.errorLabel.hide()
            if self.view.firstMatrixTab.matrix.columnCount() != self.view.secondMatrixTab.matrix.rowCount():
                raise Exception
            multiply = self.model.multiply(self.convertToSparse(self.view.firstMatrixTab.matrix),
                                           self.convertToSparse(self.view.secondMatrixTab.matrix))

            self.view.resultMatrixTab.originRow = self.view.firstMatrixTab.matrix.rowCount()
            self.view.resultMatrixTab.originColumn = self.view.secondMatrixTab.matrix.columnCount()
            self.view.resultMatrixTab.creatTable(self.view.resultMatrixTab.originRow,
                                                 self.view.resultMatrixTab.originColumn,
                                                 self.view.resultMatrixTab.matrix, multiply)

            self.view.resultMatrixTab.sparseButton.setEnabled(True)

        except:
            self.view.resultMatrixTab.errorLabel.show()

    def initSparseButton(self):
        try:
            self.view.resultMatrixTab.errorLabel.hide()
            source = self.view.sender()
            if source.text() == "Sparse":
                source.setText("Normal")
                sparse = self.convertToSparse(self.view.resultMatrixTab.matrix)
                self.view.resultMatrixTab.createSparseTabel(self.view.resultMatrixTab.matrix, sparse)

            elif source.text() == "Normal":
                source.setText("Sparse")
                matrix = [(int(self.view.resultMatrixTab.matrix.item(i, 0).text()),
                           int(self.view.resultMatrixTab.matrix.item(i, 1).text()),
                           float(self.view.resultMatrixTab.matrix.item(i, 2).text()))
                          for i in range(self.view.resultMatrixTab.originRow + 1)]

                self.view.resultMatrixTab.creatTable(self.view.resultMatrixTab.originRow,
                                                     self.view.resultMatrixTab.originColumn,
                                                     self.view.resultMatrixTab.matrix
                                                     , matrix)

        except:
            self.view.resultMatrixTab.errorLabel.show()

    def convertToSparse(self, matrix=QTableWidget):
        sparse = []
        for i in range(matrix.rowCount()):
            for j in range(matrix.columnCount()):
                if matrix.item(i, j).text() != '0':
                    sparse.append((i, j, float(matrix.item(i, j).text())))

        return sparse
