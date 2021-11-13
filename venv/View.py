from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTabWidget, QSpinBox, QTableWidget, \
    QTableWidgetItem
from PyQt6.QtCore import Qt


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setWindowTitle("Sparse Matrix")
        layout = QVBoxLayout()
        self.setLayout(layout)

        tabWidget = QTabWidget()
        tabWidget.setStyleSheet("font-size: 13px;")

        self.firstMatrixTab = FirstMatrixTab()
        self.secondMatrixTab = SecondMatrixTab()
        self.resultMatrixTab = ResultMatrixTab()

        tabWidget.addTab(self.firstMatrixTab, "First Matrix")
        tabWidget.addTab(self.secondMatrixTab, "Second Matrix")
        tabWidget.addTab(self.resultMatrixTab, "Result Matrix")

        layout.addWidget(tabWidget)


class FirstMatrixTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        upperBox = QHBoxLayout()
        self.layout.addLayout(upperBox)

        matrixDimensionsLabel = QLabel("Matrix Dimensios : ")
        matrixDimensionsLabel.setStyleSheet("font-size: 16px;")

        self.matrixRow = QSpinBox()
        self.matrixRow.setToolTip("Row")
        self.matrixRow.setMinimum(1)
        self.matrixRow.setMaximum(1000)
        self.matrixRow.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        xLabel = QLabel("\u00d7")
        xLabel.setStyleSheet("font-size: 25px;")

        self.matrixColumn = QSpinBox()
        self.matrixColumn.setToolTip("Column")
        self.matrixColumn.setMinimum(1)
        self.matrixColumn.setMaximum(1000)
        self.matrixColumn.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        self.showButton = QPushButton("Show Matrix")
        self.showButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.showButton.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 30px;
        """)

        self.transposeButton = QPushButton("Transpose")
        self.transposeButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.transposeButton.hide()
        self.transposeButton.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 15px;
        """)

        self.errorLabel = QLabel("Something went wrong!")
        self.errorLabel.hide()
        self.errorLabel.setStyleSheet("""  
            font-size: 15px;  
            color: red;
            margin-left: 30px;
        """)

        upperBox.addWidget(matrixDimensionsLabel)
        upperBox.addWidget(self.matrixRow)
        upperBox.addWidget(xLabel)
        upperBox.addWidget(self.matrixColumn)
        upperBox.addWidget(self.showButton)
        upperBox.addWidget(self.transposeButton)
        upperBox.addWidget(self.errorLabel)
        upperBox.addStretch(1)
        upperBox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.matrix = QTableWidget()
        self.layout.addWidget(self.matrix)

    def creatTable(self, row, column, matrix, items=[]):
        matrix.setRowCount(row)
        matrix.setColumnCount(column)
        matrix.setStyleSheet("font-size: 14px;")
        for i in range(row):
            for j in range(column):
                matrix.setColumnWidth(j, 25)
                matrix.setItem(i, j, QTableWidgetItem('0'))
                if items != []:
                    for k in range(len(items)):
                        if items[k][0] == i and items[k][1] == j:
                            value = items[k][2]
                            if (int(value) == value):
                                value = int(value)
                            matrix.setItem(i, j, QTableWidgetItem(str(value)))

        return matrix


class SecondMatrixTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        upperBox = QHBoxLayout()
        self.layout.addLayout(upperBox)

        matrixDimensionsLabel = QLabel("Matrix Dimensios : ")
        matrixDimensionsLabel.setStyleSheet("font-size: 16px;")

        self.matrixRow = QSpinBox()
        self.matrixRow.setToolTip("Row")
        self.matrixRow.setMinimum(1)
        self.matrixRow.setMaximum(1000)
        self.matrixRow.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        xLabel = QLabel("\u00d7")
        xLabel.setStyleSheet("font-size: 25px;")

        self.matrixColumn = QSpinBox()
        self.matrixColumn.setToolTip("Column")
        self.matrixColumn.setMinimum(1)
        self.matrixColumn.setMaximum(1000)
        self.matrixColumn.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        self.showButton = QPushButton("Show Matrix")
        self.showButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.showButton.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 30px;
        """)

        self.transposeButton = QPushButton("Transpose")
        self.transposeButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.transposeButton.hide()
        self.transposeButton.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 15px;
        """)

        self.errorLabel = QLabel("Something went wrong!")
        self.errorLabel.hide()
        self.errorLabel.setStyleSheet("""  
            font-size: 15px;  
            color: red;
            margin-left: 30px;
        """)

        upperBox.addWidget(matrixDimensionsLabel)
        upperBox.addWidget(self.matrixRow)
        upperBox.addWidget(xLabel)
        upperBox.addWidget(self.matrixColumn)
        upperBox.addWidget(self.showButton)
        upperBox.addWidget(self.transposeButton)
        upperBox.addWidget(self.errorLabel)
        upperBox.addStretch(1)
        upperBox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.matrix = QTableWidget()
        self.layout.addWidget(self.matrix)

    def creatTable(self, row, column, matrix, items=[]):
        matrix.setRowCount(row)
        matrix.setColumnCount(column)
        matrix.setStyleSheet("font-size: 14px;")
        for i in range(row):
            for j in range(column):
                matrix.setColumnWidth(j, 25)
                matrix.setItem(i, j, QTableWidgetItem('0'))
                if items != []:
                    for k in range(len(items)):
                        if items[k][0] == i and items[k][1] == j:
                            value = items[k][2]
                            if (int(value) == value):
                                value = int(value)
                            matrix.setItem(i, j, QTableWidgetItem(str(value)))

        return matrix


class ResultMatrixTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        upperBox = QHBoxLayout()
        self.layout.addLayout(upperBox)

        self.sumButton = QPushButton("Sum")
        self.sumButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.sumButton.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
        """)

        self.subButton = QPushButton("Subtract")
        self.subButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.subButton.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 15px;
        """)

        self.mulButton = QPushButton("Multipy")
        self.mulButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.mulButton.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 15px;
        """)

        self.errorLabel = QLabel("Something went wrong!")
        self.errorLabel.hide()
        self.errorLabel.setStyleSheet("""  
            font-size: 15px;  
            color: red;
            margin-left: 30px;
        """)

        upperBox.addWidget(self.sumButton)
        upperBox.addWidget(self.subButton)
        upperBox.addWidget(self.mulButton)
        upperBox.addWidget(self.errorLabel)
        upperBox.addStretch(1)
        upperBox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.matrix = QTableWidget()
        self.layout.addWidget(self.matrix)

    def creatTable(self, row, column, matrix, items=[]):
        matrix.setRowCount(row)
        matrix.setColumnCount(column)
        matrix.setStyleSheet("font-size: 14px;")
        for i in range(row):
            for j in range(column):
                matrix.setColumnWidth(j, 25)
                matrix.setItem(i, j, QTableWidgetItem('0'))
                if items != []:
                    for k in range(len(items)):
                        if items[k][0] == i and items[k][1] == j:
                            value = items[k][2]
                            if (int(value) == value):
                                value = int(value)
                            matrix.setItem(i, j, QTableWidgetItem(str(value)))

        return matrix
