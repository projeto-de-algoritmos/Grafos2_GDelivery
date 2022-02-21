from collections import defaultdict 

def init_graph():

    graph = {
        # RED nodes
            '0': {'1' : 8},
            '1': {'0' : 8, '2' : 42, '7' : 31},
            '2': {'1' : 42, '3' : 10, '4': 22, '6':30},
            '3': {'2' : 10, '4' : 25, '5': 30, '22': 36},
            '4': {'3' : 25, '2' : 22},
            '5': {'3' : 30, '6' : 31, '12' : 9, '21' : 20},
            '6': {'2' : 30, '5' : 31, '10' : 71},
            '7': {'1' : 31, '8' : 55},
            '8': {'7' : 55, '9' : 11, '13' : 36, '14' : 43},
            '9': {'8' : 11, '10' : 11, '15' : 37},
            '10': {'6': 71, '9' : 11, '11' : 12, '16' : 36},
            '11': {'10' : 12, '12' : 57, '17' : 36, '18' : 25},
            '12': {'5' : 29, '11' : 57, '19' : 11, '20' : 10},

        # GREEN nodes
            '13': {'8' : 36},
            '14': {'8' : 43},
            '15': {'9' : 37},
            '16': {'10': 36},
            '17': {'11': 36},
            '18': {'11': 25},
            '19': {'12': 11},
            '20': {'12': 10},
            '21': {'5' : 20},
            '22': {'3' : 36}
    }
            
    return graph

def dijkstra(graph, search):

    atual_node = {}; path = {}; controller = {}
    unvisiteds = []
    atual_node['0'] = 0
    atual = '0'

    
    for nodes in graph:
        unvisiteds.append(nodes)    
        path[nodes] = 999999 
    
    path[atual] = [0,'0']

    unvisiteds.remove(atual)
    #print(f'{atual} visitado')

    while unvisiteds:
        for previous, distance in graph[atual].items():
             #print(atual_node)
             peso = distance + atual_node[atual]
             #print(f'Peso aresta {atual} = {peso}')

             if path[previous] == 999999 or path[previous][0] > peso:
                 path[previous] = [peso, atual]
                 controller[previous] = peso
       
        min_node = min(controller.items(), key=lambda x: x[1])
        #print(f'Menor nó vizinho: {min_node[1]}')

        atual=min_node[0]; atual_node[atual] = min_node[1]
        
        unvisiteds.remove(atual)
        #print(f'{atual} visitado')
        del controller[atual]

    print('Node   Menor_distancia\n----------------')
    for nodes in path:
        print(f' {nodes}  ->   {path[nodes][0]}')

    print('----------------')

    small_path = [search]
    x = search

    for names in path:
        if x == '0': break

        x = path[x][1]
        small_path.append(x)
    
    print(small_path[::-1])

    return small_path[::-1]


# if __name__ == "__main__":
	
#     graph = init_graph()
#     brabissimo = dijkstra(graph, '18')

