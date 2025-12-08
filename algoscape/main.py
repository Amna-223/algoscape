from utils.display import slow_print

"""AlgoScape Main Game"""
def show_welcome():
    slow_print("Welcome to AlgoScape!")
    slow_print("You wake up in a mysterious AI research laboratory. \
            \nThe doors are locked with algorithmic puzzles. \
            \nTo escape, you must master 8 search algorithms by solving interactive challenges in each room.\
            \nYour score will be counted on the basis of your strategy")

def bfs_room(score):
    slow_print("Welcome to the first room!\n")
    try:
        from rooms.bfs_room import play_room
        room_score = play_room()
        score += room_score
        return score
    except Exception as e:
        print(f"Error in BFS room: {e}")
        return score

def dfs_room(score):
    slow_print("Welcome to the second room!\n")
    try:
        from rooms.dfs_room import play_room
        room_score = play_room()
        score += room_score
        return score
    except Exception as e:
        print(f"Error in DFS room: {e}")
        return score 

def ids_room(score):
    slow_print("Welcome to the third room!\n")
    try:
        from rooms.ids_room import play_room
        room_score = play_room()
        score += room_score
        return score
    except Exception as e:
        print(f"Error in IDS room: {e}")
        return score       

def main():
    show_welcome()
    score = 0
    roomSearched = 0
#bfs game call
    score = bfs_room(score)
    roomSearched += 1
    slow_print(f"\nTotal Score: {score}/800")
    slow_print(f"Room Searched: {roomSearched}/8")
    
#dfs game call
    score = dfs_room(score)
    roomSearched += 1
    slow_print(f"\nTotal Score: {score}/800")
    slow_print(f"Room Searched: {roomSearched}/8")

#ids game call
    score = ids_room(score)
    roomSearched += 1
    slow_print(f"\nTotal Score: {score}/800")
    slow_print(f"Rooms Searched: {roomSearched}/8")

if __name__ == "__main__":
    main()