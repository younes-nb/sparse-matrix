class Model:
    def transpose(self, A=list):
        B = [0 for i in range(len(A))]
        if (A != []):
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
        while (i < firstMatrix.__len__() and j < secondMatrix.__len__()):
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
                    result.append((firstMatrix[i][0], firstMatrix[i][1], firstMatrix[i][2] + secondMatrix[j][2]))
                    i += 1
                    j += 1

        while (i < firstMatrix.__len__()):
            result.append(firstMatrix[i])
            i += 1

        while (j < secondMatrix.__len__()):
            result.append(secondMatrix[j])
            j += 1

        return result


