# 狄克斯特拉算法
# 适用于加权图，最短路径寻找
# 只适用于有向无环图
# 不适用于包含负权边的图，原因在于已经处理过的节点的开销，会因为负边而发生变动。


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        # 如果当前节点的开销低，且未被处理过
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost  # 就将其视为最低开销的节点
            lowest_cost_node = node
    return lowest_cost_node


def dijkstras(graph, costs, parents, processed):
    node = find_lowest_cost_node(costs, processed)  # 在未处理的节点中找出开销最小的节点
    while node is not None:  # 所有节点都被处理过后结束
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  # 遍历当前节点的所有邻接点
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:  # 如果经过当前节点前往该邻居节点更近
                costs[n] = new_cost  # 更新该邻居的开销
                parents[n] = node  # 同时将该邻居的父节点设为当前节点
        processed.append(node)  # 将当前节点标记为处理过
        node = find_lowest_cost_node(costs, processed)  # 找出接下来要处理的节点，并循环


def lookup_path(parents, end="fin"):
    path = []
    path.append(end)
    while True:
        if end in parents:
            end = parents[end]
            path.append(end)
        else:
            break
    path.reverse()
    return path


if __name__ == "__main__":
    # 图
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}

    # 起点到各个节点的开销
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = float("inf")

    # 记录各个节点所耗开销对应的父节点
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    # 数组，记录处理过的节点
    processed = []

    # main process
    dijkstras(graph, costs, parents, processed)
    path = lookup_path(parents)
    print(path, costs["fin"])