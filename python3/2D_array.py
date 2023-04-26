"""Generating a 2D array."""
if __name__ == '__main__':
    cols = 5
    rows = 4
    start = 1
    # Matrix = [[0 for x in range(cols)] for y in range(rows)]
    # Matrix[0][0] = 1
    # Matrix[0][6] = 3
    # Matrix[1][1] = 5
    # Matrix[4][5] = 9

    # print(Matrix[4][5])
    # print(Matrix)

    print("Shorter way to implement 2D arrays: ")
    matrix = [[start + col + cols * row for col in range(cols)] for row in range(rows)]
        # new_matrix[1][0] = 2
    print(matrix)
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
