import game
import sys



if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "start":
        print("[Starting new game]")
        if __name__ == "__main__":
            game.main()
    elif command == "quit":
        print("Ending current game")
        
    else:
        print('Please specify "start" or "quit"')
else:
    print('''Usage:
        Start new game: python start.py start
        Create new page: python start.py quit''')