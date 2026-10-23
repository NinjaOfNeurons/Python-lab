def setZeroes(matrix):
    hor_list = [1]*len(matrix)
    ver_list = [1]*len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 :
                hor_list[i] = 0 
                ver_list[j] = 0

    print(hor_list, ver_list)
    print(matrix)

    for i in range(len(hor_list)):
        for j in range(len(ver_list)):
            if hor_list[i] == 0 or ver_list[j] == 0:
                matrix[i][j] = 0 
          
    print(matrix)


    return 0


print(setZeroes( [[1,1,1,3],
                  [1,0,1,3],
                  [1,1,0,2]]))