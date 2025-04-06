
Undo = []
Redo = []

def WRITE(X):
    Undo.append(X)

def UNDO():
    if Undo:
        X = Undo.pop()
        Redo.append(X)
    else:
        print("Nothing to UNDO.")
def REDO():
    if Redo:
        X = Redo.pop()
        Undo.append(X)
    else:
        print("Nothing to REDO.")

def READ():
    if Undo:
        print("Current Document State:", ''.join(Undo))
    else:
        print("Document is empty.")

def QUERY():
    while True:
        command = input("Enter command (WRITE X, UNDO, REDO, READ, EXIT): ").strip()
        
        if command.startswith("WRITE"):
            _, text = command.split(maxsplit=1)
            WRITE(text)
        elif command == "UNDO":
            UNDO()
        elif command == "REDO":
            REDO()
        elif command == "READ":
            READ()
        elif command == "EXIT":
            print("Exiting the program.")
            break
        else:
            print("Invalid command. Please try again.")

QUERY()
