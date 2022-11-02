def DFS(graph,v,visited):
    # 가장먼저 1번부터 방문
    visited[v]=True
    print(v)
    # i는 0부터 시작
    # print(graph[v])
    for i in range(len(graph[v])):
        node=graph[v][i]
        # print("node:",node)
        if visited[node]!=True:
            DFS(graph,node,visited)

if __name__ == '__main__':
    graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

    # 즉 9칸 짜리의 visited 생성
    visited=[False]*9

    DFS(graph,1,visited)