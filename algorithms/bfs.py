from collections import deque

class SimpleBFS:
    def __init__(self):
        self.name = "BFS"

    def create_maze(self):
        maze =  [
            ['S', '.', '#', '.', '.'],
            ['.', '.', '.', '#', '.'],
            ['#', '#', '.', '.', '.'],
            ['.', '#', '.', '#', '.'],
            ['.', '.', '.', '.', 'E']
        ]
        return maze

    def find_path(self, maze, start, end):
        rows = 5
        cols = 5
        
        queue = deque()
        queue.append((start, [start]))
        visited = set()
        visited.add(start)

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == end:
                return path
           
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols:
                    if maze[nx][ny] != "#" and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), path + [(nx, ny)]))
        
        return None

    def check_move(self, pos, move, maze):
        moves = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}

        if move not in moves:
            return False, pos, "Bad Command"

        dx, dy = moves[move]
        nx, ny = pos[0] + dx, pos[1] + dy

        if nx < 0 or nx >=5 or ny < 0 or ny >= 5:
            return False, pos, "Outside Maze"

        if maze[nx][ny] == '#':
            return False, pos, "Wall"

        return True, (nx, ny), "OK"

    def get_score(self, user_steps, best_steps):
        if user_steps == best_steps:
            return 100
        elif user_steps <= best_steps + 2:
            return 90
        elif user_steps <= best_steps + 5:
            return 80
        else:
            return 0