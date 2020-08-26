def my_dij(G,start,end):
    is_visited,father,dis = {},{},{}
    n = len(G)
    for k in G.keys():
        father[k] = start
        is_visited[k] = False
        dis[k] = G[start][k]
    is_visited[start] = True
    for _ in range(n):
        min_dis= F
        for k in G.keys():
            if not is_visited[k] and dis[k]<min_dis:
                min_dis = dis[k]
                min_node = k
        is_visited[min_node] = True
        for k in G.keys():
            if not is_visited[k] and dis[k]>dis[min_node]+G[min_node][k]:
                dis[k] = dis[min_node] + G[min_node][k]
                father[k] = min_node
    path,j = [],end
    while j!=start:
        path.append(j)
        j = father[j]
    path.reverse()
    return path,dis[end]

F=9999
G={  'a':{'a':0,'b':20,'c':F,'d':80,'e':F,'f':F,'g':90,'h':F},
    'b':{'a':F,'b':0,'c':F,'d':F,'e':F,'f':10,'g':F,'h':F},
    'c':{'a':F,'b':F,'c':0,'d':10,'e':F,'f':50,'g':F,'h':20},
    'd':{'a':F,'b':F,'c':F,'d':0,'e':F,'f':F,'g':20,'h':F},
    'e':{'a':F,'b':50,'c':F,'d':F,'e':0,'f':F,'g':30,'h':F},
    'f':{'a':F,'b':F,'c':10,'d':40,'e':F,'f':0,'g':F,'h':F},
    'g':{'a':20,'b':F,'c':F,'d':F,'e':F,'f':F,'g':0,'h':F},
    'h':{'a':F,'b':F,'c':F,'d':F,'e':F,'f':F,'g':F,'h':0}
    }
print(my_dij(G,'a','g'))