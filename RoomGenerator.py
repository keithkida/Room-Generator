import random

def generate_graph(room_count=8, branching=0.3, loops=0.1):
    rooms = [f"Room{i}" for i in range(room_count)]
    start = "Start"
    goal = "Goal"

    graph = {start: ["Room0"]}
    graph.update({room: [] for room in rooms})

    for i in range(room_count - 1):
        graph[rooms[i]].append(rooms[i + 1])
        
    
    for r in rooms:
        if random.random() < branching:
            target = random.choice(rooms)
            r_num = int(r[4:])
            t_num = int(target[4:])
            if target != r and target not in graph[r] and r_num < t_num and r_num != room_count - 1:
                graph[r].append((target, "branch"))

    for r in rooms:
        if random.random() < loops:
            target = random.choice(rooms)
            r_num = int(r[4:])
            t_num = int(target[4:])
            if target != r and target not in graph[r] and r_num > t_num and r_num != room_count - 1:
                graph[r].append((target, "loop"))

    graph[rooms[-1]].append(goal)

    
    return graph

def print_graph(graph):
    for room, edges in graph.items():
        connections = []
        for edge in edges:
            if isinstance(edge, tuple):
                connections.append(f"{edge[0]} ({edge[1]})")
            else:
                connections.append(edge)
        print(f"{room} -> {', '.join(connections)}")

if __name__ == "__main__":
    number_of_graphs = int(input("Enter number of graphs to generate: "))
    for i in range(number_of_graphs): 
        random_room_count = random.randint(5, 10)
        random_branching =  random.randint(0, 100) / 100.0
        random_loops = random.randint(0, 100) / 100.0
        print("\n") 
        graph = generate_graph( random_room_count, random_branching, random_loops ) 
        print_graph(graph)
        print(f"room_count={random_room_count}, branching chance={random_branching * 100:.2f}%, loops chance={random_loops*100:.2f}%")