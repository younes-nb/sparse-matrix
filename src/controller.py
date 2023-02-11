from view import *
from model import *
from PyQt6.QtWidgets import QTableWidget


def convert_to_sparse(matrix: QTableWidget):
    sparse = []
    for i in range(matrix.rowCount()):
        for j in range(matrix.columnCount()):
            if matrix.item(i, j).text() != '0':
                sparse.append((i, j, float(matrix.item(i, j).text())))

    return sparse


class Controller:
    def __init__(self):
        self.view = View()
        self.init_buttons()

    def init_buttons(self):
        self.view.first_matrix_tab.show_button.clicked.connect(self.init_first_show_button)
        self.view.second_matrix_tab.show_button.clicked.connect(self.init_second_show_button)
        self.view.first_matrix_tab.transpose_button.clicked.connect(self.init_first_transpose_button)
        self.view.second_matrix_tab.transpose_button.clicked.connect(self.init_second_transpose_button)
        self.view.result_matrix_tab.sum_button.clicked.connect(self.init_sum_button)
        self.view.result_matrix_tab.sub_button.clicked.connect(self.init_sub_button)
        self.view.result_matrix_tab.mul_button.clicked.connect(self.init_mul_button)
        self.view.result_matrix_tab.sparse_button.clicked.connect(self.init_sparse_button)

    def init_first_show_button(self):
        self.view.first_matrix_tab.error_label.hide()
        creat_table(
            int(self.view.first_matrix_tab.matrix_row.value()), int(self.view.first_matrix_tab.matrix_column.value()),
            self.view.first_matrix_tab.matrix)
        self.view.first_matrix_tab.transpose_button.show()

    def init_second_show_button(self):
        self.view.second_matrix_tab.error_label.hide()
        creat_table(
            int(self.view.second_matrix_tab.matrix_row.value()), int(self.view.second_matrix_tab.matrix_column.value()),
            self.view.second_matrix_tab.matrix)
        self.view.second_matrix_tab.transpose_button.show()

    def init_first_transpose_button(self):
        try:
            self.view.first_matrix_tab.error_label.hide()
            sparse = convert_to_sparse(self.view.first_matrix_tab.matrix)
            if not sparse:
                creat_table(self.view.first_matrix_tab.matrix.columnCount(),
                            self.view.first_matrix_tab.matrix.rowCount(),
                            self.view.first_matrix_tab.matrix)
            else:
                transposed_sparse = transpose(sparse)
                creat_table(self.view.first_matrix_tab.matrix.columnCount(),
                            self.view.first_matrix_tab.matrix.rowCount(),
                            self.view.first_matrix_tab.matrix, transposed_sparse)

            self.view.first_matrix_tab.matrix_row.setValue(self.view.first_matrix_tab.matrix.columnCount())
            self.view.first_matrix_tab.matrix_column.setValue(self.view.first_matrix_tab.matrix.rowCount())
        except:
            self.view.first_matrix_tab.error_label.show()

    def init_second_transpose_button(self):
        try:
            self.view.second_matrix_tab.error_label.hide()
            sparse = convert_to_sparse(self.view.second_matrix_tab.matrix)
            if not sparse:
                creat_table(self.view.second_matrix_tab.matrix.columnCount(),
                            self.view.second_matrix_tab.matrix.rowCount(),
                            self.view.second_matrix_tab.matrix)
            else:
                transposed_sparse = transpose(sparse)
                creat_table(self.view.second_matrix_tab.matrix.columnCount(),
                            self.view.second_matrix_tab.matrix.rowCount(),
                            self.view.second_matrix_tab.matrix, transposed_sparse)

            self.view.second_matrix_tab.matrix_row.setValue(self.view.second_matrix_tab.matrix.columnCount())
            self.view.second_matrix_tab.matrix_column.setValue(self.view.second_matrix_tab.matrix.rowCount())
        except:
            self.view.second_matrix_tab.error_label.show()

    def init_sum_button(self):
        try:
            self.view.result_matrix_tab.error_label.hide()
            if self.view.first_matrix_tab.matrix.rowCount() != self.view.second_matrix_tab.matrix.rowCount() or self.view.first_matrix_tab.matrix.columnCount() != self.view.second_matrix_tab.matrix.columnCount():
                raise Exception

            sum_ = summation(convert_to_sparse(self.view.first_matrix_tab.matrix),
                             convert_to_sparse(self.view.second_matrix_tab.matrix))
            self.view.result_matrix_tab.origin_row = self.view.first_matrix_tab.matrix.rowCount()
            self.view.result_matrix_tab.origin_column = self.view.first_matrix_tab.matrix.columnCount()
            creat_table(self.view.result_matrix_tab.origin_row,
                        self.view.result_matrix_tab.origin_column,
                        self.view.result_matrix_tab.matrix, sum_)

            self.view.result_matrix_tab.sparse_button.setEnabled(True)
        except Exception as e:
            print(e)
            self.view.result_matrix_tab.error_label.show()

    def init_sub_button(self):
        try:
            self.view.result_matrix_tab.error_label.hide()
            if self.view.first_matrix_tab.matrix.rowCount() != self.view.second_matrix_tab.matrix.rowCount() or self.view.first_matrix_tab.matrix.columnCount() != self.view.second_matrix_tab.matrix.columnCount():
                raise Exception

            subtraction = subtract(convert_to_sparse(self.view.first_matrix_tab.matrix),
                                   convert_to_sparse(self.view.second_matrix_tab.matrix))

            self.view.result_matrix_tab.origin_row = self.view.first_matrix_tab.matrix.rowCount()
            self.view.result_matrix_tab.origin_column = self.view.first_matrix_tab.matrix.columnCount()
            creat_table(self.view.result_matrix_tab.origin_row,
                        self.view.result_matrix_tab.origin_column,
                        self.view.result_matrix_tab.matrix, subtraction)

            self.view.result_matrix_tab.sparse_button.setEnabled(True)
        except:
            self.view.result_matrix_tab.error_label.show()

    def init_mul_button(self):
        try:
            self.view.result_matrix_tab.error_label.hide()
            if self.view.first_matrix_tab.matrix.columnCount() != self.view.second_matrix_tab.matrix.rowCount():
                raise Exception
            mul = multiply(convert_to_sparse(self.view.first_matrix_tab.matrix),
                           convert_to_sparse(self.view.second_matrix_tab.matrix))

            self.view.result_matrix_tab.origin_row = self.view.first_matrix_tab.matrix.rowCount()
            self.view.result_matrix_tab.origin_column = self.view.second_matrix_tab.matrix.columnCount()
            creat_table(self.view.result_matrix_tab.origin_row,
                        self.view.result_matrix_tab.origin_column,
                        self.view.result_matrix_tab.matrix, mul)

            self.view.result_matrix_tab.sparse_button.setEnabled(True)
        except:
            self.view.result_matrix_tab.error_label.show()

    def init_sparse_button(self):
        try:
            self.view.result_matrix_tab.error_label.hide()
            source = self.view.sender()
            if source.text() == "Sparse":
                source.setText("Normal")
                sparse = convert_to_sparse(self.view.result_matrix_tab.matrix)
                create_sparse_tabel(self.view.result_matrix_tab.matrix, sparse)

            elif source.text() == "Normal":
                source.setText("Sparse")
                matrix = [(int(self.view.result_matrix_tab.matrix.item(i, 0).text()),
                           int(self.view.result_matrix_tab.matrix.item(i, 1).text()),
                           float(self.view.result_matrix_tab.matrix.item(i, 2).text()))
                          for i in range(self.view.result_matrix_tab.origin_row + 1)]

                creat_table(self.view.result_matrix_tab.origin_row,
                            self.view.result_matrix_tab.origin_column,
                            self.view.result_matrix_tab.matrix
                            , matrix)

        except:
            self.view.result_matrix_tab.error_label.show()
