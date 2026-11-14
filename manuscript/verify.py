import argparse
from collections import deque
from itertools import combinations
import json
from pathlib import Path

import sympy as sp


def theta_graph(length):
    adjacency = [set() for vertex in range(length + 5)]
    paths = [[0, 2, 3, 1], [0, 4, 5, 1], [0, *range(6, length + 5), 1]]
    for path in paths:
        for left, right in zip(path, path[1:]):
            adjacency[left].add(right)
            adjacency[right].add(left)
    return adjacency


def distances(adjacency, start):
    result = [-1] * len(adjacency)
    result[start] = 0
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for neighbor in adjacency[vertex]:
            if result[neighbor] == -1:
                result[neighbor] = result[vertex] + 1
                queue.append(neighbor)
    return result


def symbolic_checks():
    parameter, endpoint = sp.symbols('t A')
    quadratic = parameter**2 - 1
    first = -quadratic / 2
    checks = []
    for sign in (1, -1):
        second = -((parameter + sign) * quadratic - 2 * parameter) / 2
        invariant = sp.expand(4 * (second**2 + first**2 - parameter * second * first - 1))
        factorization = sign * (parameter - 2 * sign) * quadratic * (parameter**2 + 2 * sign * parameter - 1)
        assert sp.expand(invariant - factorization) == 0
        assert sp.rem(second - sign, parameter**2 + 2 * sign * parameter - 1, parameter) == 0
        checks.append({'e': sign, 'factorization': str(sp.factor(invariant))})
    short_left, short_right, terminal, initial = sp.symbols('B C D s')
    singular = []
    expected_dimensions = [(0, 1, 0, 1), (0, 1, 1, 0), (0, 0, 0, 0),
                           (1, 1, 1, 1), (1, 1, 0, 0), (0, 0, 0, 0)]
    periods = {1: [endpoint, initial, initial - endpoint, -endpoint, -initial, endpoint - initial],
               -1: [endpoint, initial, -endpoint - initial]}
    for residue in range(6):
        for sign_index, sign in enumerate((1, -1)):
            for parameter_index, parameter_value in enumerate((1, -1)):
                period = periods[parameter_value]
                last = period[residue % len(period)]
                penultimate = period[(residue - 1) % len(period)]
                equations = [parameter_value * short_left - endpoint - short_right,
                             parameter_value * short_right - short_left - terminal,
                             initial - (parameter_value + sign) * endpoint + 2 * short_left,
                             last - terminal,
                             penultimate - (parameter_value + sign) * terminal + 2 * short_right]
                matrix, constants = sp.linear_eq_to_matrix(equations, (endpoint, short_left, short_right, terminal, initial))
                assert constants == sp.zeros(5, 1)
                dimension = 5 - matrix.rank()
                assert dimension == expected_dimensions[residue][2 * sign_index + parameter_index]
                singular.append({'r_mod_6': residue, 'e': sign, 't': parameter_value,
                                 'symmetric_dimension': dimension})
    return {'factorizations': checks, 'singular_systems': singular}


def finite_case(length):
    adjacency = theta_graph(length)
    order = len(adjacency)
    distance_matrix = [distances(adjacency, start) for start in range(order)]
    assert all(distance >= 0 for row in distance_matrix for distance in row)
    for left in range(order):
        for right in range(left + 1, order):
            assert adjacency[left] - {right} != adjacency[right] - {left}
    profiles = list(zip(distance_matrix[2], distance_matrix[6]))
    metric_dimension = 3 if length in (3, 5) else 2
    if metric_dimension == 2:
        assert len(set(profiles)) == order
        resolving_set = [2, 6]
    else:
        assert all(len({(distance_matrix[left][vertex], distance_matrix[right][vertex])
                        for vertex in range(order)}) < order
                   for left, right in combinations(range(order), 2))
        resolving_set = next(list(landmarks) for landmarks in combinations(range(order), 3)
                             if len({tuple(distance_matrix[landmark][vertex] for landmark in landmarks)
                                     for vertex in range(order)}) == order)
    if length >= 6:
        assert profiles[:6] == [(1, 1), (2, 4), (0, 2), (1, 3), (2, 2), (3, 3)]
        for position in range(1, length):
            assert profiles[position + 5] == (min(position + 1, length - position + 2),
                                              min(position - 1, length - position + 4))
    assert all(len(set(row)) < order for row in distance_matrix)
    adjacency_matrix = sp.zeros(order)
    degree_matrix = sp.zeros(order)
    for vertex, neighbors in enumerate(adjacency):
        degree_matrix[vertex, vertex] = len(neighbors)
        for neighbor in neighbors:
            adjacency_matrix[vertex, neighbor] = 1
    variable = sp.Symbol('z')
    laplacian = (degree_matrix - adjacency_matrix).charpoly(variable).as_poly()
    signless = (degree_matrix + adjacency_matrix).charpoly(variable).as_poly()
    laplacian_gcd = sp.gcd(laplacian, laplacian.diff()).monic()
    signless_gcd = sp.gcd(signless, signless.diff()).monic()
    repeated_laplacian = [[3], [3], [], [1, 3], [1, 3], []][length % 6]
    repeated_signless = [[1], [3], [], [1, 3], [], []][length % 6]
    expected_laplacian_gcd = (variable**2 - 6 * variable + 7 if length == 2 else
                              sp.expand(sp.prod(variable - value for value in repeated_laplacian)))
    assert laplacian_gcd.as_expr() == expected_laplacian_gcd
    assert signless_gcd.as_expr() == sp.expand(sp.prod(variable - value for value in repeated_signless))
    for polynomial, repeated in [(laplacian, repeated_laplacian), (signless, repeated_signless)]:
        for value in repeated:
            assert polynomial.eval(value) == 0
            assert polynomial.diff().eval(value) == 0
            assert polynomial.diff().diff().eval(value) != 0
    if length == 2:
        census_labels = [1, 4, 2, 3, 6, 5, 7]
        census_edges = {tuple(sorted((census_labels[left], census_labels[right])))
                        for left, neighbors in enumerate(adjacency) for right in neighbors}
        assert census_edges == {(1, 2), (1, 6), (1, 7), (2, 3), (3, 4), (4, 5), (4, 7), (5, 6)}
        expected_laplacian = variable * (variable - 1) * (variable - 3) * (variable**2 - 6 * variable + 7)**2
        quadratic = variable**2 - 4 * variable + 1
        cubic = variable**3 - 8 * variable**2 + 17 * variable - 8
        expected_signless = (variable - 1) * (variable - 3) * quadratic * cubic
        assert sp.expand(laplacian.as_expr() - expected_laplacian) == 0
        assert sp.expand(signless.as_expr() - expected_signless) == 0
        assert sp.discriminant(quadratic, variable) == 12
        assert sp.discriminant(cubic, variable) == 316
        assert sp.rem(cubic, quadratic, variable) == -4
        assert sp.gcd(laplacian_gcd, laplacian_gcd.diff()).degree() == 0
        assert sp.div(laplacian, laplacian_gcd**2)[1].is_zero
        assert sp.gcd(sp.div(laplacian, laplacian_gcd**2)[0], laplacian_gcd).degree() == 0
    multiplicity_at_two = 1 if signless.eval(2) == 0 else 0
    assert multiplicity_at_two == int(length % 4 == 1)
    if multiplicity_at_two:
        assert signless.diff().eval(2) != 0
    laplacian_maximum = 2 if length == 2 or repeated_laplacian else 1
    signless_maximum = 2 if repeated_signless else 1
    assert (laplacian_maximum == metric_dimension and signless_maximum != metric_dimension) == (length == 2 or length % 6 == 4)
    assert not (signless_maximum == metric_dimension and laplacian_maximum != metric_dimension)
    return {'r': length, 'vertices': order, 'edges': sum(map(len, adjacency)) // 2,
            'connected': True, 'twin_free': True, 'metric_dimension': metric_dimension,
            'resolving_set_vertex_indices': resolving_set,
            'maximum_laplacian_multiplicity': laplacian_maximum,
            'maximum_signless_multiplicity': signless_maximum,
            'laplacian_repeated_eigenvalues': ['3-sqrt(2)', '3+sqrt(2)'] if length == 2 else repeated_laplacian,
            'signless_repeated_eigenvalues': repeated_signless,
            'signless_multiplicity_at_2': multiplicity_at_two,
            'gcd_chi_L_derivative': str(laplacian_gcd.as_expr()),
            'gcd_chi_Q_derivative': str(signless_gcd.as_expr())}


def rooted_path_checks():
    variable = sp.Symbol('z')
    results = []
    for name, order, basis, expected in [('K133', 7, [1, 2, 4, 5], (4, 4, 5)),
                                         ('K2_join_2K2', 6, [0, 2, 4], (3, 2, 3))]:
        base = [set() for vertex in range(order)]
        parts = [{0}, {1, 2, 3}, {4, 5, 6}] if name == 'K133' else None
        for left, right in combinations(range(order), 2):
            connected = (not any(left in part and right in part for part in parts)) if parts else (
                left < 2 or right < 2 or {left, right} in ({2, 3}, {4, 5}))
            if connected:
                base[left].add(right)
                base[right].add(left)
        base_distance = [distances(base, vertex) for vertex in range(order)]
        outside = [tuple(base_distance[landmark][vertex] for landmark in basis)
                   for vertex in range(order) if vertex not in basis]
        assert all(len(set(first - second for first, second in zip(left, right))) > 1
                   for left, right in combinations(outside, 2))
        for length in range(1, 5):
            adjacency = [set(neighbors) for neighbors in base] + [set() for vertex in range(order * length)]
            for root in range(order):
                path = [root] + [order + root * length + depth for depth in range(length)]
                for left, right in zip(path, path[1:]):
                    adjacency[left].add(right)
                    adjacency[right].add(left)
            landmarks = [order + root * length + length - 1 for root in basis]
            rows = [distances(adjacency, landmark) for landmark in landmarks]
            assert len(set(zip(*rows))) == len(adjacency)
            assert all(distance >= 0 for row in rows for distance in row)
            for left, right in combinations(range(len(adjacency)), 2):
                assert adjacency[left] - {right} != adjacency[right] - {left}
            matrix = sp.zeros(len(adjacency))
            degree = sp.zeros(len(adjacency))
            for vertex, neighbors in enumerate(adjacency):
                degree[vertex, vertex] = len(neighbors)
                for neighbor in neighbors:
                    matrix[vertex, neighbor] = 1
            spectra = {}
            for label, graph_matrix, target in [('L', degree - matrix, expected[1]),
                                                 ('Q', degree + matrix, expected[2])]:
                polynomial = graph_matrix.charpoly(variable).as_poly()
                factors = sp.factor_list(polynomial)[1]
                multiplicity = max(exponent for factor, exponent in factors)
                assert multiplicity == target
                spectra[label] = {'characteristic_factors': str(sp.factor(polynomial.as_expr())),
                                  'maximum_multiplicity': multiplicity}
            results.append({'base': name, 'path_edges': length, 'order': len(adjacency),
                            'resolving_set': landmarks, 'metric_dimension': expected[0],
                            'metric_lower_bound': 'Projection to the base and its twin classes.',
                            'outside_base_profiles': outside, 'spectra': spectra})
    return results


def main():
    parser = argparse.ArgumentParser(description='Exact checks for theta(3,3,r), r >= 2.')
    parser.add_argument('--output', type=Path)
    arguments = parser.parse_args()
    result = {'schema_version': 1, 'arithmetic': 'exact integers and rational polynomials',
              'sympy_version': sp.__version__, 'symbolic': symbolic_checks(),
              'finite_scope': 'Every integer r from 2 through 40; includes k = 1,...,6 in r = 6k+4.',
              'cases': [finite_case(length) for length in range(2, 41)],
              'rooted_paths': rooted_path_checks(),
              'coverage': 'Symbolic identities, all 24 singular systems, exceptional length-two factors, 39 theta graphs and eight rooted-path graphs; the all-parameter statements have written proofs in note.tex.'}
    text = json.dumps(result, indent=2) + '\n'
    if arguments.output:
        arguments.output.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
