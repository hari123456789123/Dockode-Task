def honey_comp(rows, columns):


    for i in range(rows):
        if i == rows- 1:
            print(' ___')
        else:
            print(' ___    ', end="")


    for i in range(rows):

        for j in range(rows):
            if j == rows - 1:
                print('/   \\')
            else:
                print('/   \\___', end="")


        for j in range(rows):
            if j == rows - 1:
                print('\\___/')
            else:
                print('\\___/   ', end="")

honey_comp(3, 5)