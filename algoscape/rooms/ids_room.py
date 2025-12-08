"""
Room 3: IDS Memory Challenge
"""
from algorithms.ids import SimpleIDS
from utils.display import slow_print

def play_room():
    print("\n" + "=" * 50)
    slow_print("ROOM 3: IDS MEMORY CHALLENGE")
    print("=" * 50)
    
    slow_print("\nSTORY:")
    slow_print("Your memory is limited! You can only remember")
    slow_print("2 steps back. Find the secret number (15)")
    slow_print("by exploring this number tree.")
    
    slow_print("\nHOW TO PLAY:")
    slow_print("Start from number 1")
    slow_print("Move to child numbers only (1→2, 1→3)")
    slow_print("Can't remember parent - only last 2 steps")
    slow_print("Type number to move, 'back' to go back")
    slow_print("'map' to see current depth tree")
    slow_print("'quit' to exit")
    
    ids = SimpleIDS()
    tree = ids.create_number_tree()
    
    start = '1'
    goal = '15'
    current = start
    
    user_path = [start]
    steps = 0
    depth_limit = 2
    memory_stack = []
    extra_depth_tries = 0
    
    print(f"\nYou start at: {start}")
    print(f"Find number: {goal}")
    print(f"Memory limit: Remember last {depth_limit} steps only")
    
    while True:
        print(f"\nCurrent: {current}")
        print(f"Steps taken: {steps}")
        print(f"Memory: {memory_stack[-depth_limit:] if memory_stack else 'Empty'}")
        
        if current == goal:
            slow_print(f"\nFOUND IT! Number {goal}!")
            slow_print(f"Total steps: {steps}")
            slow_print(f"Extra depth attempts: {extra_depth_tries}")
            break
        
        valid_moves = ids.get_valid_moves(current, tree, memory_stack)
        
        if valid_moves:
            print(f"Next numbers: {', '.join(valid_moves)}")
        else:
            print("Dead end! Must go back.")
            valid_moves = ['back']
        
        command = input("\nGo to number (or 'back'/'map'/'quit'): ").strip().lower()
        
        if command == 'quit':
            print("\nExiting...")
            return 0
        
        elif command == 'back':
            if memory_stack:
                current = memory_stack.pop()
                user_path.append(current)
                steps += 1
                print(f"Back to {current}")
            else:
                print("Can't go back further!")
            continue
        
        elif command == 'map':
            print("\nNumber Tree (showing from current):")
            print_tree_from(current, tree)
            continue
        
        if command in valid_moves:
            memory_stack.append(current)
            if len(memory_stack) > depth_limit:
                memory_stack.pop(0)  
            
            current = command
            user_path.append(current)
            steps += 1
            
            current_depth = calculate_depth(current, tree)
            if current_depth > depth_limit:
                extra_depth_tries += 1
                print(f"Warning: Going deep! Memory fading")
    
            print(f"Moved to {current}")
            
        
        else:
            print(f"Can't go to {command} from here!")
    
    optimal_path, optimal_depth = ids.find_optimal_path(tree, start, goal)
    
    # Calculate how many times the optimal path exceeds depth limit
    optimal_extra_depth = sum(1 for node in optimal_path if calculate_depth(node, tree) > depth_limit)
    
    score = ids.calculate_score(user_path, optimal_path, depth_limit, extra_depth_tries, optimal_extra_depth)
    
    print("\n" + "=" * 50)
    slow_print("RESULTS:")
    print("=" * 50)
    
    print(f"\nYour Path ({len(user_path)} steps):")
    for num in user_path:
        print(num, end=' -> ')
    print()
    
    print(f"IDS Optimal Path ({len(optimal_path)} steps, depth {optimal_depth}):")
    print(" → ".join(optimal_path))
    
    slow_print(f"\nSTATS:")
    slow_print(f"Your steps: {steps}")
    slow_print(f"Optimal steps: {len(optimal_path)-1}")
    slow_print(f"Memory limit: {depth_limit}")
    slow_print(f"Extra depth tries: {extra_depth_tries}")
    slow_print(f"Score: {score}/100")
    
    return score

def calculate_depth(node, tree):
    """Calculate depth of node in tree"""
    depth = 0
    current = node
    while current != '1':
        for parent, children in tree.items():
            if current in children:
                current = parent
                depth += 1
                break
        else:
            break
    return depth

def print_tree_from(node, tree, max_depth=3):
    """Print tree starting from current node"""
    def print_level(current, level, visited, prefix="", is_last=True):
        if level > max_depth or current in visited:
            return
        
        visited.add(current)
        
        # Print current node with proper tree characters
        if level == 0:
            print(f"{current}")
        else:
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{current}")
        
        # Get children
        children = tree.get(current, [])
        
        # Print each child
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            
            # Prepare prefix for children
            if level == 0:
                new_prefix = ""
            else:
                extension = "    " if is_last else "│   "
                new_prefix = prefix + extension
            
            print_level(child, level + 1, visited, new_prefix, is_last_child)
    
    print_level(node, 0, set())