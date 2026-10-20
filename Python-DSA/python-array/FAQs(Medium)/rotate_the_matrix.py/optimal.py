


def rotate90(matrix):
    n = len(matrix)

    # transposing the matrix 
    for i in range(n):
        for j in range(i+1):
            if i != j:
                # print(matrix[i][j], matrix[j][i])
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

    print(matrix)

    #  reversing each row 
    for i , row in enumerate(matrix):
        matrix[i] = row[::-1]

        print(matrix)
            
    return matrix






matrix = [[0, 1, 1, 2],
          [2, 0, 3, 1],
          [4, 5, 0, 5],
          [5, 6, 7, 0]]

print(rotate90(matrix))
             




