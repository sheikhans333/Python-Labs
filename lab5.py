#q1
def bfs(graph,current_node):
    queue=[]
    queue.append(current_node)
    visited=[]
    visited.append(current_node)
    while queue:
        node=queue.pop(0)
        print(node,end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
        
graph={
    '0': ['1', '2', '3'],
    '1': ['4', '5'],
    '2': ['6','7'],
    '3': ['7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}
bfs(graph,'0')
print()
print("-----------------------------------------------------------------------------------")
#q2
def bfs(graph,current_node,find_node):
    queue=[]
    queue.append(current_node)
    visited=[]
    visited.append(current_node)
    while queue:
        node=queue.pop(0)
        print(node,end=" ")
        if node==find_node:
            return True
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
        
graph={
    '0': ['1', '2', '3'],
    '1': ['4', '5'],
    '2': ['6','7'],
    '3': ['7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}
if bfs(graph,'0','5'):
    print("Node found")
else:
    print("Node not found")
print()
print("---------------------------------------------------------------------------")

#q3
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        
        self.queue.append((priority, item))
        self.queue.sort()

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)[1]
        else:
            raise IndexError("dequeue from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


pq = PriorityQueue()
pq.enqueue("task1", 2) 
pq.enqueue("task2", 1)  
pq.enqueue("task3", 3)  

while not pq.is_empty():
    print(pq.dequeue())
