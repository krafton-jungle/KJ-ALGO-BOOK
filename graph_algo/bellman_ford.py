def bellman_ford(edges, V, start):
    distance = [float('inf')] * V
    distance[start] = 0
    
    for _ in range(V+1):
        for u,v,w in edges:
            if distance[u] != float('inf') and distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                
    for u,v,w in edges:
        if distance[u] != float('inf') and distance[v] > distance[u] + w:
            raise ValueError("There's an negative Cycle")
        
    return distance