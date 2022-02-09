#Describe the graph 
Graph_nodes = {
                'A': [('B', 2), ('E', 3)],
                'B': [('C', 1),('G', 9)],
                'C': [],
                'E': [('D', 6)],
                'D': [('G', 1)],
                'G': []
              }

#Heuristic Distance
H_dist = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0,
             
        }

g = {} #stores distance from starting node

parents = {} # Contains parent node

def f(n):
    return g[n] + H_dist[n]

#This function gives the path, applying A* algorithm on graph
def aStarAlgo(start_node, stop_node):
         
        open_set = set(start_node) #create open set and add start_node to it
        closed_set = set()
 
        #distance of start node from itself is zero
        g[start_node] = 0

        #start_node is root node i.e it has no parent nodes
        #so start_node is set to its own as parent node
        parents[start_node] = start_node

#--------------------------------------------------------------------
        while len(open_set) > 0:

            n = None

            #-----------------------------------------------------
            #node with lowest f() is equated to n in this for loop
            for v in open_set:
                if n == None or f(v) < f(n):
                    n = v

            #-------------------------------------------------------
            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                path = []
 
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
 
                path.append(start_node)
 
                path.reverse()        
                print('Path found: {}'.format(path))
                return path

            #---------------------------------------------------
            if Graph_nodes[n] == None:
                pass
            else:
                for (child, dist) in Graph_nodes[n]:

                    #if child node is not in open and close set then add it to open set
                    #then update it's parent node, and g distance
                    if child not in open_set and child not in closed_set:
                        open_set.add(child)
                        parents[child] = n
                        g[child] = g[n] + dist
                         
                    #--------------------------------------------------
                    #it will check and change for the optimal value of a g[n] or path length
                    
                    #This part is exicuted when the path changes and the current 
                    # g distance is less than the previous one.
                    # Here g distance is updated
                    elif g[child] > g[n] + dist:
                            #update g(m)
                            g[child] = g[n] + dist
                            #change parent of m to n
                            parents[child] = n
                        #--------------------------------------------    
                            #After changing path length if the node is in closed set then remove it
                            #and put it in open set
                            if child in closed_set:
                                closed_set.remove(child)
                                open_set.add(child)


                #--------------------------------------------------------
                                
                    # remove n from the open_list, and add it to closed_list
                    # because all of his neighbors were inspected
                open_set.remove(n)
                closed_set.add(n)


        #if everything fails
        print('Path does not exist!')
        return None

aStarAlgo('A', 'G')   
