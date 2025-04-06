📝 Command-Line Text Editor with Undo/Redo

A simple command-line-based text editor that supports undo and redo functionality using stack data structures.
🚀 Features

    ✅ Write text word by word

    🔄 Undo the last write

    🔁 Redo the undone text

    🧠 Pure logic-based (no GUI)

    ⚙️ Implemented using Python and Stacks

🧰 Technologies Used

    Language: Python

    Data Structures: Stack (List in Python)

    Interface: Command-line

    Version Control: Git & GitHub

🧠 How It Works

    WRITE X → Adds X to the text and stores the previous state in Undo stack.

    UNDO → Removes the last written word and moves it to Redo stack.

    REDO → Restores the last undone word.

    READ → Displays the current document.

    EXIT → Exits the program.

📦 Sample Usage

Enter command (WRITE X, UNDO, REDO, READ, EXIT): WRITE Hello
Enter command (WRITE X, UNDO, REDO, READ, EXIT): WRITE World
Enter command (WRITE X, UNDO, REDO, READ, EXIT): READ
Current Document State: HelloWorld
Enter command (WRITE X, UNDO, REDO, READ, EXIT): UNDO
Enter command (WRITE X, UNDO, REDO, READ, EXIT): READ
Current Document State: Hello
Enter command (WRITE X, UNDO, REDO, READ, EXIT): REDO
Enter command (WRITE X, UNDO, REDO, READ, EXIT): READ
Current Document State: HelloWorld

🏗️ Project Structure

text_editor.py         # Main logic of the editor
README.md              # Project documentation

📚 Concepts Used

    Stack operations: push, pop

    String manipulation

    Command parsing

    State tracking

