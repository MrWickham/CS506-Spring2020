import math

def euclidean_dist(x, y):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    # raise NotImplementedError()

    '''
    if len(x) != len(y):
        raise ValueError("not good values")
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i]) ** 2
    return res ** (1/2)
    '''

def manhattan_dist(x, y):
    return sum(abs(a-b) for a,b in zip(x,y))
    # raise NotImplementedError()

def jaccard_dist(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return 1 - intersection_cardinality/float(union_cardinality)
    # raise NotImplementedError()

def cosine_sim(x, y):
    def square_rooted(x):
        return round(math.sqrt(sum([a*a for a in x])),3)

    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)
    # raise NotImplementedError()

# Feel free to add more
