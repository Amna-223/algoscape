"""
Iterative Deepening Search Algorithm
"""
class SimpleIDS:
    def __init__(self):
        self.name = "IDS"
    
    def create_number_tree(self):
        """Create a number tree for IDS"""
        tree = {
            '1': ['2', '3'],
            '2': ['4', '5'],
            '3': ['6', '7'],
            '4': ['8', '9'],
            '5': ['10', '11'],
            '6': ['12', '13'],
            '7': ['14', '15'],
            '8': [], '9': [], '10': [], '11': [],
            '12': [], '13': [], '14': [], '15': []
        }
        return tree
    
    def find_with_depth_limit(self, tree, start, goal, depth_limit):
        """Find path with depth limit (IDS core)"""
        def depth_limited_search(node, goal, depth):
            if depth == 0:
                return None
            if node == goal:
                return [node]
            
            for neighbor in tree.get(node, []):
                result = depth_limited_search(neighbor, goal, depth - 1)
                if result is not None:
                    return [node] + result
            return None
        
        return depth_limited_search(start, goal, depth_limit)
    
    def find_optimal_path(self, tree, start, goal):
        """IDS: Keep increasing depth limit"""
        depth = 1
        while True:
            path = self.find_with_depth_limit(tree, start, goal, depth)
            if path:
                return path, depth
            depth += 1
            if depth > 10:
                return None, depth
    
    def get_valid_moves(self, current, tree, memory):
        """Get moves within memory limit"""
        return tree.get(current, [])
    
    def calculate_score(self, user_path, optimal_path, depth_limit, extra_depth_penalty, optimal_extra_depth):
        """Calculate IDS score, penalize unnecessary depth violations"""
        
        # Factor 1: Path Efficiency
        if len(user_path) == len(optimal_path):
            efficiency = 70
        elif len(user_path) <= len(optimal_path) + 2:
            efficiency = 60
        elif len(user_path) <= len(optimal_path) + 5:
            efficiency = 50
        else:
            efficiency = 0

        print("Efficiency: ", efficiency)
        
        # Factor 2: Depth Management
        unnecessary_depth_tries = max(0, extra_depth_penalty - optimal_extra_depth)
        
        if unnecessary_depth_tries == 0:
            depth_score = 30
        elif unnecessary_depth_tries <= 2:
            depth_score = 20
        elif unnecessary_depth_tries <= 5:
            depth_score = 10
        else:
            depth_score = 0

        print("Depth Score: ", depth_score)
        
        return efficiency + depth_score