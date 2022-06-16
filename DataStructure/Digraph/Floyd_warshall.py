from copy import deepcopy

def floyd_warshall(g): # g-graph 입력
    closure = deepcopy(g)
    vertices = list(closure.vertices()) # closure의 노드들을 list 형식으로 받음
    n = len(vertices)
    
    for k in range(n):
        for i in range(n):
            if i!=k and closure.get_edge(vertices[i],vertices[k]) is not None:
                # i와 k가 같다는 것은 같은 vertex를 가리키는 것이기에 달라야 함 AND vertex i와 k 사이에 edge가 있어야 함
                for j in range(n):
                    if i!=j!=k and closure.get_edge(vertices[k],vertices[j]) is not None:
                        # i, j, k 각각 서로 다른 vertex를 가리키고 있어야 함 AND vertex k와 j 사이에 edge가 있어야 함
                        if closure.get_edge(vertices[i],vertices[j]) is None:
                            # 만약 vertex i와 j 사이에 edge가 없으면 추가한다.
                            closure.insert_edge(vertices[i],vertices[j])
    return closure