from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTabWidget, QSpinBox, \
    QTableWidget, QTableWidgetItem


class View(QWidget):
    def __init__(self):
        super(View, self).__init__()
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setWindowTitle("Sparse Matrix")
        layout = QVBoxLayout()
        self.setLayout(layout)

        tab_widget = QTabWidget()
        tab_widget.setStyleSheet("font-size: 13px;")

        self.first_matrix_tab = MatrixTab()
        self.second_matrix_tab = MatrixTab()
        self.result_matrix_tab = ResultMatrixTab()

        tab_widget.addTab(self.first_matrix_tab, "First Matrix")
        tab_widget.addTab(self.second_matrix_tab, "Second Matrix")
        tab_widget.addTab(self.result_matrix_tab, "Result Matrix")

        layout.addWidget(tab_widget)


class MatrixTab(QWidget):
    def __init__(self):
        super(MatrixTab, self).__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        upper_box = QHBoxLayout()
        self.layout.addLayout(upper_box)

        matrix_dimensions_label = QLabel("Matrix Dimensios : ")
        matrix_dimensions_label.setStyleSheet("font-size: 16px;")

        self.matrix_row = QSpinBox()
        self.matrix_row.setToolTip("Row")
        self.matrix_row.setMinimum(1)
        self.matrix_row.setMaximum(1000)
        self.matrix_row.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        x_label = QLabel("\u00d7")
        x_label.setStyleSheet("font-size: 25px;")

        self.matrix_column = QSpinBox()
        self.matrix_column.setToolTip("Column")
        self.matrix_column.setMinimum(1)
        self.matrix_column.setMaximum(1000)
        self.matrix_column.setStyleSheet("""  
            font-size: 14px; 
            padding: 3px;
        """)

        self.show_button = QPushButton("Show Matrix")
        self.show_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.show_button.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 30px;
        """)

        self.transpose_button = QPushButton("Transpose")
        self.transpose_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.transpose_button.hide()
        self.transpose_button.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 15px;
        """)

        self.error_label = QLabel("Something went wrong!")
        self.error_label.hide()
        self.error_label.setStyleSheet("""  
            font-size: 15px;  
            color: red;
            margin-left: 30px;
        """)

        upper_box.addWidget(matrix_dimensions_label)
        upper_box.addWidget(self.matrix_row)
        upper_box.addWidget(x_label)
        upper_box.addWidget(self.matrix_column)
        upper_box.addWidget(self.show_button)
        upper_box.addWidget(self.transpose_button)
        upper_box.addWidget(self.error_label)
        upper_box.addStretch(1)
        upper_box.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.matrix = QTableWidget()
        self.layout.addWidget(self.matrix)


def create_sparse_tabel(matrix, sparse):
    row = sparse.__len__()
    column = 3
    matrix.setRowCount(row)
    matrix.setColumnCount(column)
    matrix.setStyleSheet("font-size: 14px;")
    for i in range(row):
        for j in range(column):
            matrix.setColumnWidth(j, 25)
            if int(sparse[i][2]) == sparse[i][2]:
                matrix.setItem(i, j, QTableWidgetItem(str(int(sparse[i][j]))))
            else:
                matrix.setItem(i, j, QTableWidgetItem(str(sparse[i][j])))


def creat_table(row, column, matrix, items=None):
    if items is None:
        items = []
    matrix.setRowCount(row)
    matrix.setColumnCount(column)
    matrix.setStyleSheet("font-size: 14px;")
    for i in range(row):
        for j in range(column):
            matrix.setColumnWidth(j, 25)
            matrix.setItem(i, j, QTableWidgetItem('0'))
            if items:
                for k in range(len(items)):
                    if items[k][0] == i and items[k][1] == j:
                        value = items[k][2]
                        if int(value) == value:
                            value = int(value)
                        matrix.setItem(i, j, QTableWidgetItem(str(value)))

    return matrix


class ResultMatrixTab(QWidget):
    def __init__(self):
        super(ResultMatrixTab, self).__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        upper_box = QHBoxLayout()
        self.layout.addLayout(upper_box)

        self.sum_button = QPushButton("Sum")
        self.sum_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.sum_button.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
        """)

        self.sub_button = QPushButton("Subtract")
        self.sub_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.sub_button.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 15px;
        """)

        self.mul_button = QPushButton("Multipy")
        self.mul_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.mul_button.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 15px;
        """)

        self.sparse_button = QPushButton("Sparse")
        self.sparse_button.setDisabled(True)
        self.sparse_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.sparse_button.setStyleSheet("""  
            font-size: 15px; 
            padding: 6px; 
            margin-left: 15px;
        """)

        self.error_label = QLabel("Something went wrong!")
        self.error_label.hide()
        self.error_label.setStyleSheet("""  
            font-size: 15px;  
            color: red;
            margin-left: 30px;
        """)

        upper_box.addWidget(self.sum_button)
        upper_box.addWidget(self.sub_button)
        upper_box.addWidget(self.mul_button)
        upper_box.addWidget(self.sparse_button)
        upper_box.addWidget(self.error_label)
        upper_box.addStretch(1)
        upper_box.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.matrix = QTableWidget()
        self.layout.addWidget(self.matrix)
        self.origin_row = 0
        self.origin_column = 0
