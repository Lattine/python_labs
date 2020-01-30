def bfs(graph, start_name, check_fn):
    # graph 图
    # start_name 开始节点名称
    # check_fn 检查函数
    from collections import deque

    search_queue = deque()  # 创建一个队列
    search_queue += graph[start_name]  # 将开始节点的邻接点加入队列
    searched = []  # 数组用于记录检查过的节点
    while search_queue:  # 如果队列不为空
        item = search_queue.popleft()  # 出队列一个元素
        if item not in searched:  # 仅当该元素为被遍历过
            if check_fn(item):  # 终止条件，如节点具有某个特征
                print(f"stop at {item}")
                return True
            else:  # 否则，将该节点的所有邻接点加入队列
                search_queue += graph.get(item, [])

    return False  # 最终未找到满足条件的节点


if __name__ == "__main__":
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["alice"] = ["anuj", "peggy"]
    graph["bob"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["thom"] = []

    def person_name_contain_m(name):
        return "m" in name

    bfs(graph, "you", person_name_contain_m)
