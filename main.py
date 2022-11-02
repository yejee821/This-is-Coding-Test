from collections import deque

def BFS(graph,v,visited):
    queue=deque()
    visited[v]=True
    queue.append(v)

    for t in range(8):
        # print("queue: ",queue)
        now = queue.popleft()
        print(now)
        for i in range(len(graph[now])):
            node=graph[now][i]
            if visited[node]==False:
                visited[node]=True
                queue.append(node)


if __name__ == '__main__':
    graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

    visited=[False]*9

    BFS(graph,1,visited)