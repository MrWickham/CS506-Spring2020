from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    n = len(points)
    x = sum([p[0] for p in points]) / n
    y = sum([p[1] for p in points]) / n
    return [x, y]


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    k = max(assignments) + 1
    clusters = [[] for i in range(k)]
    for i, index in enumerate(assignments):
        clusters[index].append(dataset[i])

    new_centers = []
    for cluster in clusters:
        new_centers.append(point_avg(cluster))

    return new_centers

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return sum([(a - b) ** 2 for a, b in zip(a, b)]) ** 0.5


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return random.sample(dataset, k)


def cost_function(clustering):
    cost = 0
    for idx in clustering:
        center = point_avg(clustering[idx])
        cost += sum([distance(center, p) ** 2 for p in clustering[idx]])

    return cost


def generate_k_pp(dataset, k):
    raise NotImplementedError()


def do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    k_points = generate_k(dataset, k)
    return do_lloyds_algo(dataset, k_points)



def k_means_pp(dataset, k):
    k_points = generate_k_pp(dataset, k)
    return do_lloyds_algo(dataset, k_points)


filepath = "/mnt/c/lwh/cs/20spring/506/CS506-Spring2020/02-library/tests/test_files/dataset_1_k_is_2_0.csv"

from cs506 import read
dataset = read.read_csv(filepath)

k_means(dataset, 5)