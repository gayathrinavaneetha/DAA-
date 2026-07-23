import pytest

from daa.greedy import (
    assignment_problem,
    build_huffman_codes,
    decode_huffman,
    optimal_bst,
    vertex_cover,
    vertex_cover_max_degree,
)


def test_optimal_bst_cost():
    cost, root = optimal_bst([10, 12, 16, 21], [4, 2, 6, 3])
    assert cost[0][3] == 26
    assert root[0][3] == 2


def test_optimal_bst_two_keys():
    cost, _ = optimal_bst([10, 12], [34, 50])
    assert cost[0][1] == 118


def test_optimal_bst_single_key():
    cost, root = optimal_bst(["A"], [0.5])
    assert cost[0][0] == 0.5
    assert root[0][0] == 0


def test_vertex_cover_is_valid_cover():
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
    cover = set(vertex_cover(6, edges))
    assert all(u in cover or v in cover for u, v in edges)


def test_vertex_cover_max_degree_is_valid_cover():
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 5), (4, 5)]
    cover = set(vertex_cover_max_degree(7, edges))
    assert all(u in cover or v in cover for u, v in edges)


def test_vertex_cover_max_degree_picks_hub():
    # Star graph: centre 0 connected to everything -> optimal cover is {0}.
    edges = [(0, 1), (0, 2), (0, 3), (0, 4)]
    assert vertex_cover_max_degree(5, edges) == [0]


def test_assignment_problem():
    cost_matrix = [[10, 2, 8], [10, 4, 7], [3, 5, 9]]
    assignment, cost = assignment_problem(cost_matrix)
    assert cost == 12
    assert assignment == (1, 2, 0)


def test_assignment_problem_identity():
    cost_matrix = [[1, 9], [9, 1]]
    assignment, cost = assignment_problem(cost_matrix)
    assert cost == 2
    assert assignment == (0, 1)


def test_build_huffman_codes_assigns_by_frequency_order():
    characters = ["a", "b", "c", "d"]
    frequencies = [5, 9, 12, 13]
    code_dict = build_huffman_codes(characters, frequencies)
    assert set(code_dict) == set(characters)
    # Codes are the binary index in ascending-frequency order.
    assert code_dict == {"a": "0", "b": "1", "c": "10", "d": "11"}


def test_decode_huffman_greedy():
    # These coursework codes are not prefix-free, so decoding is greedy and
    # a re-encode does not round-trip; assert the actual greedy behaviour.
    code_dict = {"a": "0", "b": "1", "c": "10", "d": "11"}
    assert decode_huffman("011011", code_dict) == "abbabb"
    assert decode_huffman("0", code_dict) == "a"


def test_decode_huffman_empty():
    code_dict = build_huffman_codes(["a", "b"], [1, 2])
    assert decode_huffman("", code_dict) == ""
