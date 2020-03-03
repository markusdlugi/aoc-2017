import networkx as nx


# Manual approach
def get_connected(curr, visited):
    if curr in visited or curr not in pipes:
        return None
    result = set()
    result.add(curr)
    visited.add(curr)
    for connection in pipes[curr]:
        connections = get_connected(connection, visited)
        if connections is not None and connections:
            result = result.union(connections)
    return result


pipes = {}
for line in open("input/12.txt"):
    source, dests = line.strip().split(" <-> ")
    pipes[source] = dests.split(", ")

print(len(get_connected('0', set())))

groups = 0
while pipes:
    groups += 1
    any_index = next(iter(pipes.items()))[0]
    programs = get_connected(any_index, set())
    for program in programs:
        pipes.pop(program)
print(groups)
print()


# NetworkX
graph = nx.Graph()
for line in open("input/12.txt"):
    source, dests = line.strip().split(" <-> ")
    graph.add_edges_from((source, dest) for dest in dests.split(", "))

print(len(nx.node_connected_component(graph, '0')))
print(nx.number_connected_components(graph))
