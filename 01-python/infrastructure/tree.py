def draw_tree(height = 5):
    """
        draw a tree:
          o
         ooo
        ooooo
          o

        :param: height: the height of tree
    """

    MIN_HEIGHT = 3

    # height check
    if (height < MIN_HEIGHT) :
        raise ValueError("Invalid height, tree height must be greater than " + str(MIN_HEIGHT) + ".")

    else :
        print("found a beautiful tree.")

        # print tree
        for i in range(0, height) :
            print(" " * (height - i), end = "")
            print("o" * (2*i + 1))

        # print tree trunk
        for i in range(0, int(height / 3)):
            print (" " * int((2*height + 1)/2), end = "")
            print("o")

        return
