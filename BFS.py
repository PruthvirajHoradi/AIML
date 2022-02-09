graph = {

    5 : [3 , 7],
    3 : [2 , 4],
    7 : [8],
    4 : [8],
    2 : [],
    8 : [],
}

visited = [] #List to keep track of visited nodes
queue = [] #List of child nods which are not visited

def BFS(graph,root):

    visited.append(root)
    queue.append(root) #root is added because it's children are not visited yet

    while queue:

        s = queue.pop(0)
        print(s, end = " ")

        for child in graph[s]:
            if child not in visited:
                visited.append(child)
                queue.append(child)

BFS(graph,5)
