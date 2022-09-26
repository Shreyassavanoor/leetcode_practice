def dfs(dic, nodes, cost, visited):
    for child in nodes:
        if child in visited:
            continue
        visited.add(child)
        cost = dfs(dic, dic[child], cost + 1, visited)
    return cost

def calculate_cost(graph):
    graph_nodes = {}
    result = []
    for nodes in graph:
        des = None
        for index, g in enumerate(nodes):
            if g not in graph_nodes:
                graph_nodes[g] = []
            if index == 0:
                des = g
            else:
                graph_nodes[g].append(des)
    
    for key, value in graph_nodes.items():
        if(len(value)):
            visited_nodes = set()
            app_cost = dfs(graph_nodes, value, 1, visited_nodes)
        else:
            app_cost = 1
        result.append(key+','+str(app_cost))
    
    result.sort()
    print(result)

if __name__ == "__main__":
    calculate_cost([['A','E','N','S'], ['S','H','N'], ['E','N'],['H'],['N']])
    calculate_cost([['A','B']])
