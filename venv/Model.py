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


# value = 2.2
# if (int(value) == value):
#     value = int(value)
# print(value)
# model = Model()
# model.transpose([(0, 1, 5), (0, 4, 5.2), (1, 0, -7), (3, 4, 4)])
