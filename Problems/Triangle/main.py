import math

#What this function does is distinguish between different disjoint sets and assign a number to that.
def connectedSum(graph_nodes, graph_from, graph_to):
    visited = {}
    for i in range(graph_nodes):
        visited[i+1] = 0
    count = 1
    for i in range(len(graph_from)):
        if(visited[graph_from[i]] == 0 and visited[graph_to[i]] == 0):
            visited[graph_from[i]] = count
            visited[graph_to[i]] = count
            count += 1
        elif(visited[graph_from[i]] == 0 and visited[graph_to[i]] > 0):
            visited[graph_from[i]] = visited[graph_to[i]]
        elif(visited[graph_from[i]] > 0 and visited[graph_to[i]] == 0):
            visited[graph_to[i]] = visited[graph_from[i]]
        elif(visited[graph_from[i]] > 0 and visited[graph_to[i]] > 0):
            temp = visited[graph_to[i]]
            for x in range(graph_nodes):
                if(visited[x+1] == temp):
                    visited[x+1] = visited[graph_from[i]]

    #Calculating nodes in a set, here all isolated nodes are counted together and assigned in node_count[0]
    node_count = [0] * (graph_nodes+1)
    for x in range(graph_nodes):
        node_count[visited[x+1]] += 1

    #Calculating answer
    ans = 0
    for x in range(1,graph_nodes,1):
        ans += math.ceil(node_count[x] ** 0.5)

    return ans + node_count[0]

#Driver Code
graph_nodes = 16
graph_from = [6,9,11,15,13,12,15,1]
graph_to = [11,5,9,9,15,14,16,16]

sum = connectedSum(graph_nodes, graph_from, graph_to)

print(sum)
