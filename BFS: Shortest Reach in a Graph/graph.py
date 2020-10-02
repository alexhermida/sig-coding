from collections import defaultdict, deque


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adjacent_nodes = defaultdict(list)
        self.distances = [-1] * self.nodes  # default distances

    def connect(self, source_node, target_node):
        self.adjacent_nodes[source_node].append(target_node)
        self.adjacent_nodes[target_node].append(source_node)

    def find_all_distances(self, root_node):
        dq = deque()
        root_distance_value = 0
        dq.append((root_node, root_distance_value))

        while dq:
            node, distance = dq.popleft()

            if self.distances[node] == -1:  # first visit to the node
                self.distances[node] = distance
                # loop over node edges and add it to the queue
                [dq.append((n, distance + 6)) for n in self.adjacent_nodes.get(node, [])]

        del self.distances[root_node]
        print(*self.distances, sep=' ')