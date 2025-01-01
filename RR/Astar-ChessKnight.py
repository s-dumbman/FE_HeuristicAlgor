import heapq
import json

def load_grid(filename="grid.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data["grid"], data["start"], data["goal"]

grid, s, g = load_grid()

class Node:
    def __init__(self, x, y, g=0, h=0):
        self.x = x 
        self.y = y 
        self.g = g  
        self.h = h 
        self.f = g + h  
        self.parent = None  

    def __lt__(self, other):
        return self.f < other.f
    
def heuristic(node1, node2):
    return ((node1.x-node2.x)**2+(node1.y-node2.y)**2)**(1/2)

def search(grid, s, g):
    OL = []
    CL = set()

    s_node = Node(s[0], s[1])
    g_node = Node(g[0], g[1])

    heapq.heappush(OL, s_node)

    while OL:
        c_node = heapq.heappop(OL)
        CL.add((c_node.x, c_node.y))

        if c_node.x == g_node.x and c_node.y == g_node.y:
            return reconstruct(c_node)

        for dx, dy in [(2,1), (1,2), (-2,1), (-1,2), (2,-1), (1,-2), (-2,-1), (-1,-2)]:
            n_x = c_node.x + dx
            n_y = c_node.y + dy

            if (0 <= n_x < len(grid)) and (0 <= n_y < len(grid[0])) and grid[n_x][n_y] == 0:
                if (n_x, n_y) in CL:
                    continue

                n = Node(n_x, n_y)
                n.g = c_node.g + (5)**(1/2)
                n.h = heuristic(n, g_node)
                n.f = n.g + n.h
                n.parent = c_node

                in_open = False
                for open_node in OL:
                    if (n.x, n.y) == (open_node.x, open_node.y) and n.g >= open_node.g:
                        in_open = True
                        break

                if not in_open:
                    heapq.heappush(OL, n)

    return None

def reconstruct(end_node):
    path = []
    c = end_node
    while c is not None:
        path.append((c.x, c.y))
        c = c.parent
    path.reverse()
    return path

def mark_path_on_grid(grid, path):
    for x, y in path:
        grid[x][y] = 2 
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(['⬜️' if cell == 0 else '⬛️' if cell == 1 else '🟩' for cell in row]))

if __name__ == "__main__":
    path = search(grid, s, g)
    if path:
        grid_with_path = mark_path_on_grid(grid, path)
        print_grid(grid_with_path)
        print("경로:", path, f"{len(path)} 번")
    else:
        print("불가능한 경우")
