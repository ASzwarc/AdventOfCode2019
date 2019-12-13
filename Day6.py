import re
import networkx as nx
from networkx.algorithms import approximation

def parse_input(filename):
    input_list = []
    pattern = re.compile(r"(\S{3})\)(\S{3})")

    with open(filename) as file:
        unique_orbits = set()
        for line in file.readlines():
            orbit_one, orbit_two = re.match(pattern, line).group(1, 2)
            unique_orbits.add(orbit_one)
            unique_orbits.add(orbit_two)
            input_list.append((orbit_one, orbit_two))
    return input_list, unique_orbits


def solution(input_list, unique_orbits):
    # port one of the solution
    graph = nx.DiGraph()
    graph.add_edges_from(input_list)
    center_orbit = "COM"
    orbit_count_checksum = 0
    for orbit in unique_orbits:
        result = nx.shortest_path_length(graph, source=center_orbit,
                                         target=orbit)
        orbit_count_checksum += result
        print(f"{center_orbit}->{orbit} = {result} ({orbit_count_checksum})")
    print(f"ORBIT COUNT CHECKSUM = {orbit_count_checksum}")

    # part two of the solution
    uni_graph = nx.Graph(graph)
    result = nx.shortest_path_length(uni_graph, source="YOU", target="SAN") - 2
    print(f"Minimum number of orbital transfers is {result}")

if __name__ == '__main__':
    input_list, unique_orbits = parse_input("Day6Input.txt")
    # Test input
    # input_list = [("COM", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"),
    #               ("B", "G"), ("G", "H"), ("D", "I"), ("E", "J"), ("J", "K"),
    #               ("K", "L")]
    # unique_orbits = set(['COM', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    #                      'K', 'L'])
    solution(input_list, unique_orbits)
