import pytest

from cs506 import sim

def test_euclidean():
    assert sim.euclidean_dist([0,0], [1,0]) == 1
    assert sim.euclidean_dist([0,0,0], [1,0,0]) == 1
    assert sim.euclidean_dist([0,0,0], [0,0,0]) == 0

def test_manhattan():
    assert sim.manhattan_dist([0,0], [1,1]) == 2
    assert sim.manhattan_dist([0,0,0], [1,1,1]) == 3

def test_cosine():
    assert sim.cosine_sim([1,0], [1,0]) == 1
    assert sim.cosine_sim([0,1,0], [1,0,0]) == 0

def test_jaccard():
    assert sim.jaccard_dist([0,0], [1,0]) == .5
    assert sim.jaccard_dist([0,0,0], [1,1,1]) == 1
