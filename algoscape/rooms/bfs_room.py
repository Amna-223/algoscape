from algoscape.algorithms.bfs import SimpleBFS
from algoscape.utils.display import slow_print

def play_room():
    print("\nBFS Maze Game")
    print("Find path from S to E")
    print("Use U/D/L/R to move (Up/Down/Left/Right)")
    print("Type 'quit' to exit")

    bfs = SimpleBFS()
    maze = bfs.create_maze()
    start = (0, 0)
    end = (4, 4)

    player = start
    steps = 0
    path = [start]

    while True: #this loop will show the position of the player while playing the game
        print("\nMaze:")
        for i in range(5):
            line = ""
            for j in range(5):
                if (i, j) == player:
                    line += "@"
                else:
                    line += maze[i][j]
            print(line)

        if player == end:
            print("\nYou found the exit!")
            print("Steps taken:", steps)
            break

        move = input("\nMove (u/d/l/r): ").lower()
        if move == "quit":
            print("\nYou quit the game.")
            return 0

        ans , new_pos, msg = bfs.check_move(player, move, maze)
        if ans:
            player = new_pos
            steps += 1
            path.append(player)

        else:
            print("Invalid move:", msg)

    best_path = bfs.find_path(maze, start, end)
    best_steps = len(best_path) - 1
    score = bfs.get_score(steps, best_steps)
    
    slow_print(f"\nYour steps: {steps}")
    slow_print(f"BFS best: {best_steps}")
    slow_print(f"Score: {score}/100")

    return score