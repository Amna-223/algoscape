from algorithms.dfs import SimpleDFS
from utils.display import slow_print

def play_room():
    print("\n" + "=" * 50)
    slow_print("ROOM 2: DFS LABYRINTH")
    print("=" * 50)
    
    slow_print("\nSTORY:")
    slow_print("Find the treasure key in the deepest room.")
    slow_print("DFS goes deep first, then backtracks.")
    slow_print("Minimize backtracking for higher score!")
    
    slow_print("\nHOW TO PLAY:")
    slow_print("Type room name to move there")
    slow_print("'back' to go to previous room")
    slow_print("'map' to see connections")
    slow_print("'quit' to exit")

    dfs = SimpleDFS()
    labyrinth = dfs.create_labyrinth()
    start_room = 'Entrance'
    goal_room = 'Treasure_Room'
    current_room = start_room

    user_path = [start_room]
    steps = 0
    backtrack_count = 0
    previous_room = None

    slow_print("\nYou are at: Entrance")
    slow_print("Goal: Find key in Treasure_Room (deepest room)")

    while True:
        print(f"Current Room: {current_room}")
        print(f"Steps: {steps}")

        if current_room == goal_room:
            slow_print("\nCONGRATULATIONS! You found the treasure key!")
            slow_print(f"Total steps: {steps}")
            slow_print(f"Backtracks: {backtrack_count}")
            break

        valid_moves = dfs.get_valid_move(current_room, labyrinth)
        slow_print(f"Exits: {', '.join(valid_moves)}")

        command = input("\nWhere to go? ").strip()
        if command == 'quit':
            print("\nExiting game...")
            return 0
        elif command == 'back':
            if len(user_path) > 1:
                previous = user_path[-2]
                current_room = previous
                user_path.append(current_room)
                steps += 1
                backtrack_count += 1
                print(f"Backtracked to {current_room}")
            else:
                print("Can't go back further!")
            continue
        elif command == 'map':
            print("\nLABYRINTH MAP:")
            for room, exits in labyrinth.items():
                print(f"  {room}: {exits}")
            continue

        if command in valid_moves:
            # Track if this is backtracking
            if previous_room and command == previous_room:
                backtrack_count += 1
            previous_room = current_room
            current_room = command
            user_path.append(current_room)
            steps += 1
            print(f"Moved to {current_room}")

            if steps % 3 == 0:
                print("DFS Hint: Going deep first reduces backtracking!")

        else:
            print("Invalid move. Try again.")
            continue
    optimal_path = dfs.find_deepest_path(labyrinth, start_room, goal_room)
    score = dfs.calculate_score(user_path, optimal_path, backtrack_count)

    print("\nYour path:")
    for room in user_path:
        print(room, end=' -> ')
    print()

    print("\nOptimal path:")
    for room in optimal_path:
        print(room, end=' -> ')
    print()

    slow_print(f"\nYour steps: {steps}")
    slow_print(f"Optimal steps: {len(optimal_path)-1}")
    slow_print(f"Backtracks: {backtrack_count}")
    slow_print(f"DFS Labyrinth Score: {score}/100")

    return score