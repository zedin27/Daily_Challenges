"""Generating a 2D array."""
if __name__ == '__main__':
    col = 8
    row = 5
    Matrix = [[0 for x in range(col)] for y in range(row)]
    Matrix[0][0] = 1
    Matrix[0][6] = 3
    Matrix[1][1] = 5
    Matrix[4][5] = 9

    print(Matrix[4][5])
    print(Matrix)

    print("Shorter way to implement 2D arrays: ")
    new_matrix = [[1]* col for i in range(5)]
        # new_matrix[1][0] = 2
    print(new_matrix)
    # print("Now let us try to do inputted 2D arrays")
    #
    # rows = int(input('Enter cols\n'))
    # cols = int(input('Enter rows\n'))
    #
    # new_matrix = []
    # for i in range(cols):
    #     row = []
    #     for j in range(rows):
    #         row.append(0)
    #     new_matrix.append(row)
    #
    # print(new_matrix)
