from collections import defaultdict 

def init_graph():
# RED nodes
    graph = {'0': ['1'],
            '1': ['0', '2', '7'],
            '2': ['1', '3', '4', '6'],
            '3': ['2', '4', '5', '22'],
            '4': ['3', '2'],
            '5': ['3','6', '12', '21'],
            '6': ['2', '5', '7'],
            '7': ['1', '8'],
            '8': ['7', '9', '14', '13'],
            '9': ['8', '10', '15'],
            '10': ['6', '9', '11', '16'],
            '11': ['10', '10', '17', '18'],
            '12': ['5', '11', '19', '20'],

# GREEN nodes
            '13': ['8'],
            '14': ['8'],
            '15': ['9'],
            '16': ['10'],
            '17': ['11'],
            '18': ['11'],
            '19': ['12'],
            '20': ['12'],
            '21': ['5'],
            '22': ['3']}
            
    return graph


def BFS(graph, posInicio): 
    print("-----BFS-----")

    visited = [False] * (len(graph)) 
    lista = [] 
    lista.append(posInicio) 
    visited[posInicio] = True

    while lista: 

        posInicio = lista.pop(0) 
        print(f'{posInicio}  ->', end='  ') 

        for i in graph[posInicio]: 
            if visited[i] == False: 
                lista.append(i) 
                visited[i] = True
    print("Done!")
    return


def BFS_short_path(graph, end):
	visited = []	
	queue = [['0']]
	var_break = 0
	goal = []

	while queue:
		if(var_break == -1):
			break

		path = queue.pop(0)
		node = path[-1]
		#print(f'pop - > {path}', end='   ')
		
		if node not in visited:
			near_edges = graph[node]
			
			for edge in near_edges:
				new_path = list(path)
				new_path.append(edge)
				queue.append(new_path)
				
				if edge == end:
					print("Menor caminho = ", *new_path)
					goal = new_path
					var_break = -1
                    
			visited.append(node)

	return goal


# if __name__ == "__main__":
	
#     graph = init_graph()


#     BFS_short_path(graph, '16')
