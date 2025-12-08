import random

class SimpleDFS:
    def __init__(self):
        self.name = self

    def create_labyrinth(self):
        labyrinth = {
            "Entrance" : ["Hall"],
            'Hall': ['Entrance', 'Left_Path', 'Right_Path'],
            'Left_Path': ['Hall', 'Dead_End'],
            'Dead_End': ['Left_Path'],
            'Right_Path': ['Hall', 'Deep_Room', 'Side_Room'],
            'Side_Room': ['Right_Path'],
            'Deep_Room': ['Right_Path', 'Treasure_Room'],
            'Treasure_Room': ['Deep_Room']
        }
        return labyrinth

    def find_deepest_path(self, graph, start, goal):
        stack = [(start, [start])]
        visited = set()
        
        while stack:
            room, path = stack.pop()
            if room in visited:
                continue

            visited.add(room)
            if room == goal:
                return path

            for neighbour in reversed(graph.get(room, [])):
                if neighbour not in visited:
                    stack.append((neighbour, path + [neighbour]))
        return None

    def get_valid_move(self, current_room, labyrinth):
        return labyrinth.get(current_room, [])

    def calculate_score(self, user_path, optimal_path, backtrack_count):
        if len(user_path) == len(optimal_path):
            efficiency = 70
        elif len(user_path) <= len(optimal_path) + 2:
            efficiency = 60
        elif len(user_path) <= len(optimal_path) + 5:
            efficiency = 50
        else:
            efficiency = 0


        if backtrack_count == 0:
            dfs_style = 30
        elif backtrack_count <= 2:
            dfs_style = 20
        elif backtrack_count <= 5:
            dfs_style = 10
        else:
            dfs_style = 0
    
        return efficiency + dfs_style
        
