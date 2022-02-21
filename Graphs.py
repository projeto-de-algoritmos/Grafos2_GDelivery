from collections import defaultdict 

def init_graph():
# RED nodes
    graph = {'0': {'1' : 10},
            '1': {'0' : 10, '2' : 20},
            '2': {'1' : 20, '3' : 40, '4': 50, '6':60},
            '3': {'2' : 40, '4' : 70, '5': 80},
            '4': {'3' : 70, '2' : 50},
            '5': {'3' : 80, '6' : 100},
            '6': {'2' : 60, '5' : 100}
            # '7': {'1', '8'},
            # '8': {'7', '9'},
            # '9': {'8', '10'},
            # '10': {'6', '9', '11'},
            # '11': {'10', '10'},
            # '12': {'5', '11'}
    }

# # GREEN nodes
#             '13': ['8'],
#             '14': ['8'],
#             '15': ['9'],
#             '16': ['10'],
#             '17': ['11'],
#             '18': ['11'],
#             '19': ['12'],
#             '20': ['12'],
#             '21': ['5'],
#             '22': ['3']}
            
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
             print(atual_node)
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


if __name__ == "__main__":
	
    graph = init_graph()
    brabissimo = dijkstra(graph, '6')

