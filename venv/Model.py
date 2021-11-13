class Model:
    def transpose(self, A=list):
        B = [0 for i in range(len(A))]

        if A != []:
            originRowB = 0
            originColumnB = 0

            for item in A:

                if item[0] > originColumnB:
                    originColumnB = item[0]

                if item[1] > originRowB:
                    originRowB = item[1]

            originRowB += 1
            originColumnB += 1
            rowSize = [0 for i in range(originRowB)]

            for i in range(len(A)):
                rowSize[A[i][1]] += 1

            startOfRow = [0]

            for i in range(1, originRowB):
                startOfRow.append(startOfRow[i - 1] + rowSize[i - 1])

            for i in range(len(A)):
                x = startOfRow[A[i][1]]
                B[x] = (A[i][1], A[i][0], A[i][2])
                startOfRow[A[i][1]] += 1

            return B

    def sum(self, firstMatrix=list, secondMatrix=list):
        result = []
        i, j = 0, 0

        while i < firstMatrix.__len__() and j < secondMatrix.__len__():

            if firstMatrix[i][0] < secondMatrix[j][0]:
                result.append(firstMatrix[i])
                i += 1

            elif firstMatrix[i][0] > secondMatrix[j][0]:
                result.append(secondMatrix[j])
                j += 1

            else:

                if firstMatrix[i][1] < secondMatrix[j][1]:
                    result.append(firstMatrix[i])
                    i += 1

                elif firstMatrix[i][1] > secondMatrix[j][1]:
                    result.append(secondMatrix[j])
                    j += 1

                else:

                    if firstMatrix[i][2] + secondMatrix[j][2] != 0:
                        result.append((firstMatrix[i][0], firstMatrix[i][1], firstMatrix[i][2] + secondMatrix[j][2]))
                    i += 1
                    j += 1

        while i < firstMatrix.__len__():
            result.append(firstMatrix[i])
            i += 1

        while j < secondMatrix.__len__():
            result.append(secondMatrix[j])
            j += 1

        return result

    def subtract(self, firstMatrix=list, secondMatrix=list):
        result = []
        i, j = 0, 0

        while i < firstMatrix.__len__() and j < secondMatrix.__len__():

            if firstMatrix[i][0] < secondMatrix[j][0]:
                result.append(firstMatrix[i])
                i += 1

            elif firstMatrix[i][0] > secondMatrix[j][0]:
                result.append((secondMatrix[j][0], secondMatrix[j][1], secondMatrix[j][2] * -1))
                j += 1

            else:

                if firstMatrix[i][1] < secondMatrix[j][1]:
                    result.append(firstMatrix[i])
                    i += 1

                elif firstMatrix[i][1] > secondMatrix[j][1]:
                    result.append((secondMatrix[j][0], secondMatrix[j][1], secondMatrix[j][2] * -1))
                    j += 1

                else:

                    if firstMatrix[i][2] - secondMatrix[j][2] != 0:
                        result.append((firstMatrix[i][0], firstMatrix[i][1], firstMatrix[i][2] - secondMatrix[j][2]))
                    i += 1
                    j += 1

        while i < firstMatrix.__len__():
            result.append(firstMatrix[i])
            i += 1

        while j < secondMatrix.__len__():
            result.append((secondMatrix[j][0], secondMatrix[j][1], secondMatrix[j][2] * -1))
            j += 1

        return result

    def multiply(self, firstMatrix=list, secondMatrix=list):
        result = []
        secondMatrix = self.transpose(secondMatrix)
        i = 0

        while i < firstMatrix.__len__():
            row = firstMatrix[i][0]
            j = 0

            while j < secondMatrix.__len__():
                column = secondMatrix[j][0]
                sum = 0
                temp_i, temp_j = i, j

                while temp_i < firstMatrix.__len__() and firstMatrix[temp_i][0] == row and \
                        temp_j < secondMatrix.__len__() and secondMatrix[temp_j][0] == column:

                    if firstMatrix[temp_i][1] < secondMatrix[temp_j][1]:
                        temp_i += 1

                    elif firstMatrix[temp_i][1] > secondMatrix[temp_j][1]:
                        temp_j += 1

                    else:
                        sum += firstMatrix[temp_i][2] * secondMatrix[temp_j][2]
                        temp_i += 1
                        temp_j += 1

                if sum != 0:
                    result.append((firstMatrix[i][0], secondMatrix[j][0], sum))

                while j < secondMatrix.__len__() and secondMatrix[j][0] == column:
                    j += 1

            while i < firstMatrix.__len__() and firstMatrix[i][0] == row:
                i += 1

        return result
