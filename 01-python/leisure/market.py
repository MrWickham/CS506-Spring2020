def drawHorizontalLines(length):
    print()

    for _ in range(length):
        print("=", end="")
    print()

    print()
    

def drawFruitMarket(length):
    print("Apple || Banana || Orange".center(length))


def drawFoodMarket(length):
    print("Meet || Vegetable".center(length))


def draw_market(length = 36, category = "food"):
    """
    draw a food / fruit market with centering text.

    :param: length: the length of the horizontal line, as well as the total width of the text string

    :param: category: specifying the category of the market
    """
    MIN_LEN = 30
    VALID_CATEGORIES = ["food", "fruit"]

    # length check
    if length < MIN_LEN:
        errStr = "Length must be greater than or equal to " + str(MIN_LEN) + "."
        raise ValueError(errStr)

    # category check
    if category not in VALID_CATEGORIES:
        raise ValueError("The category is not defined.")
    
    # print stuff
    print()
    print((category.capitalize() + " Market").center(length))
    drawHorizontalLines(length)
    if category == "food":
        drawFoodMarket(length)  
    else:
        drawFruitMarket(length)
    drawHorizontalLines(length)
    return