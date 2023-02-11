def transpose(matrix: list):
    result = [0 for i in range(len(matrix))]

    if matrix:
        origin_row = 0
        origin_column = 0

        for item in matrix:
            if item[0] > origin_column:
                origin_column = item[0]

            if item[1] > origin_row:
                origin_row = item[1]

        origin_row += 1
        origin_column += 1
        row_size = [0 for i in range(origin_row)]

        for i in range(len(matrix)):
            row_size[matrix[i][1]] += 1

        start_of_row = [0]

        for i in range(1, origin_row):
            start_of_row.append(start_of_row[i - 1] + row_size[i - 1])

        for i in range(len(matrix)):
            x = start_of_row[matrix[i][1]]
            result[x] = (matrix[i][1], matrix[i][0], matrix[i][2])
            start_of_row[matrix[i][1]] += 1

        return result


def summation(first_matrix: list, second_matrix: list):
    result = []
    i, j = 0, 0

    while i < first_matrix.__len__() and j < second_matrix.__len__():
        if first_matrix[i][0] < second_matrix[j][0]:
            result.append(first_matrix[i])
            i += 1

        elif first_matrix[i][0] > second_matrix[j][0]:
            result.append(second_matrix[j])
            j += 1

        else:
            if first_matrix[i][1] < second_matrix[j][1]:
                result.append(first_matrix[i])
                i += 1

            elif first_matrix[i][1] > second_matrix[j][1]:
                result.append(second_matrix[j])
                j += 1

            else:
                if first_matrix[i][2] + second_matrix[j][2] != 0:
                    result.append((first_matrix[i][0], first_matrix[i][1], first_matrix[i][2] + second_matrix[j][2]))
                i += 1
                j += 1

    while i < first_matrix.__len__():
        result.append(first_matrix[i])
        i += 1

    while j < second_matrix.__len__():
        result.append(second_matrix[j])
        j += 1

    return result


def subtract(first_matrix: list, second_matrix: list):
    result = []
    i, j = 0, 0

    while i < first_matrix.__len__() and j < second_matrix.__len__():
        if first_matrix[i][0] < second_matrix[j][0]:
            result.append(first_matrix[i])
            i += 1

        elif first_matrix[i][0] > second_matrix[j][0]:
            result.append((second_matrix[j][0], second_matrix[j][1], second_matrix[j][2] * -1))
            j += 1

        else:
            if first_matrix[i][1] < second_matrix[j][1]:
                result.append(first_matrix[i])
                i += 1

            elif first_matrix[i][1] > second_matrix[j][1]:
                result.append((second_matrix[j][0], second_matrix[j][1], second_matrix[j][2] * -1))
                j += 1

            else:
                if first_matrix[i][2] - second_matrix[j][2] != 0:
                    result.append((first_matrix[i][0], first_matrix[i][1], first_matrix[i][2] - second_matrix[j][2]))
                i += 1
                j += 1

    while i < first_matrix.__len__():
        result.append(first_matrix[i])
        i += 1

    while j < second_matrix.__len__():
        result.append((second_matrix[j][0], second_matrix[j][1], second_matrix[j][2] * -1))
        j += 1

    return result


def multiply(first_matrix: list, second_matrix: list):
    result = []
    second_matrix = transpose(second_matrix)
    i = 0

    while i < first_matrix.__len__():
        row = first_matrix[i][0]
        j = 0
        while j < second_matrix.__len__():
            column = second_matrix[j][0]
            sum_of_row = 0
            temp_i, temp_j = i, j

            while temp_i < first_matrix.__len__() and first_matrix[temp_i][0] == row and \
                    temp_j < second_matrix.__len__() and second_matrix[temp_j][0] == column:

                if first_matrix[temp_i][1] < second_matrix[temp_j][1]:
                    temp_i += 1

                elif first_matrix[temp_i][1] > second_matrix[temp_j][1]:
                    temp_j += 1

                else:
                    sum_of_row += first_matrix[temp_i][2] * second_matrix[temp_j][2]
                    temp_i += 1
                    temp_j += 1

            if sum_of_row != 0:
                result.append((first_matrix[i][0], second_matrix[j][0], sum_of_row))

            while j < second_matrix.__len__() and second_matrix[j][0] == column:
                j += 1

        while i < first_matrix.__len__() and first_matrix[i][0] == row:
            i += 1

    return result
