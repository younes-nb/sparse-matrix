from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout, QDialog, \
    QTabWidget, QSpinBox,QTableWidget,QTableWidgetItem
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
        layout = QVBoxLayout()
        self.setLayout(layout)

        dimensionsBox = QHBoxLayout()
        layout.addLayout(dimensionsBox)

        matrixDimensionsLabel = QLabel("Matrix Dimensios : ")
        matrixDimensionsLabel.setStyleSheet("font-size: 16px;")

        self.matrixWidth = QSpinBox()
        self.matrixWidth.setMinimum(1)
        self.matrixWidth.setMaximum(100)
        self.matrixWidth.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        xLabel = QLabel("\u00d7")
        xLabel.setStyleSheet("font-size: 25px;")

        self.matrixHeight = QSpinBox()
        self.matrixHeight.setMinimum(1)
        self.matrixHeight.setMaximum(100)
        self.matrixHeight.setStyleSheet("""  
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

        dimensionsBox.addWidget(matrixDimensionsLabel)
        dimensionsBox.addWidget(self.matrixWidth)
        dimensionsBox.addWidget(xLabel)
        dimensionsBox.addWidget(self.matrixHeight)
        dimensionsBox.addWidget(self.showButton)
        dimensionsBox.addStretch(1)
        dimensionsBox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.matrix = self.addTable(10,10)
        layout.addWidget(self.matrix)

    def addTable(self,x,y):
        pass


class SecondMatrixTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        dimensionsBox = QHBoxLayout()
        layout.addLayout(dimensionsBox)

        matrixDimensionsLabel = QLabel("Matrix Dimensios : ")
        matrixDimensionsLabel.setStyleSheet("font-size: 16px;")

        self.matrixWidth = QSpinBox()
        self.matrixWidth.setMinimum(1)
        self.matrixWidth.setMaximum(100)
        self.matrixWidth.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        xLabel = QLabel("\u00d7")
        xLabel.setStyleSheet("font-size: 25px;")

        self.matrixHeight = QSpinBox()
        self.matrixHeight.setMinimum(1)
        self.matrixHeight.setMaximum(100)
        self.matrixHeight.setStyleSheet("""  
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

        dimensionsBox.addWidget(matrixDimensionsLabel)
        dimensionsBox.addWidget(self.matrixWidth)
        dimensionsBox.addWidget(xLabel)
        dimensionsBox.addWidget(self.matrixHeight)
        dimensionsBox.addWidget(self.showButton)
        dimensionsBox.addStretch(1)
        dimensionsBox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.matrix = self.addTable(10, 10)

    def addTable(self,x,y):
        pass


class ResultMatrixTab(QWidget):
    def __init__(self):
        super().__init__()
