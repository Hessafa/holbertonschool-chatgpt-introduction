# holbertonschool-chatgpt-introduction
This Project is for Enhancing Code Quality and Efficiency with ChatGPT- Debugging
    
## Task 0 
    
### given code 
```
#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
    return result

f = factorial(int(sys.argv[1]))
print(f)
```

### ChatGPT Degugging :
The issue in your factorial.py script is that the while loop never updates the value of n, which results in an infinite loop. You're multiplying result *= n repeatedly, but since n never decreases, the condition n > 1 is always true.

✅ Fix
You need to decrement n inside the loop
**see the file factorial.py**
🧪 Example Output
```bash
$ ./factorial.py 5
120

$ ./factorial.py 0
1
This fixed version correctly computes the factorial by decrementing n in each iteration.
```

</details>

## Task 1

### given code 
```
#!/usr/bin/python3
import sys

for i in range(len(sys.argv)):
    print(sys.argv[i])
```

### ChatGPT Degugging :
**See the file print_arguments.py**
```
#!/usr/bin/python3
import sys

for arg in sys.argv[1:]:
    print(arg)

```
### 🧪 Example Output
```bash
$ ./print_arguments.py 1 2 3
1
2
3
This version skips the script name and only prints the actual arguments.
```

## Task 2

### given code 
```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Change Background Color</title>
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        padding-top: 50px;
    }
    button {
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
</style>
</head>
<body>

<h2>Click the button to change the background color</h2>

<button id="colorButon">Change Color</button>

<script>
    document.getElementById("colorButton").addEventListener("click", function() {
        changeBackgroundColor();
    });

    function changeBackgroundColor() {
        // Generate a random color
        var randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
        // Change the background color of the body
        document.body.style.backgroundColor = randomColor;
    }
</script>

</body>
</html>
```
### ChatGPT Degugging :
The issue in your code is a typo in the id of the button and the corresponding getElementById method. You have defined the button's id as colorButon (with a missing "t") but are trying to select it using colorButton (with the correct spelling).

✅ Fix
Change the id of the button to colorButton.

Alternatively, you can update the getElementById call to colorButon, but it's better to make them consistent.

**See the file change_background.html**
```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Change Background Color</title>
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        padding-top: 50px;
    }
    button {
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
</style>
</head>
<body>

<h2>Click the button to change the background color</h2>

<button id="colorButton">Change Color</button>

<script>
    document.getElementById("colorButton").addEventListener("click", function() {
        changeBackgroundColor();
    });

    function changeBackgroundColor() {
        // Generate a random color
        var randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
        // Change the background color of the body
        document.body.style.backgroundColor = randomColor;
    }
</script>

</body>
</html>

```
🧪 What Changed:
The button element now has id="colorButton".

The JavaScript method document.getElementById("colorButton") correctly matches the button's id.

This should now work properly, and clicking the button will change the background color to a random one.

<img src="https://github.com/user-attachments/assets/a1ae2abd-ebdb-475d-9073-8de99a39fa50" width="400"/>


## Task 3

### given code 
```
#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

```

### ChatGPT Degugging :

The current implementation of your Minesweeper game does not check if all non-mine cells have been revealed to declare a win. To fix this, we need to add logic that monitors how many non-mine cells have been revealed and compares that with the total number of non-mine cells. If they match, the game should declare a win.

Steps to Implement the Fix:
Count the total non-mine cells when initializing the game.

Track how many non-mine cells have been revealed as the player progresses.

Check for a win condition: if the number of revealed non-mine cells is equal to the number of non-mine cells, the player wins.
**✅ Fixed Code see file mines.py**

🧪 Explanation of Changes:
self.total_non_mine_cells: This keeps track of how many non-mine cells are in the game, which is calculated as width * height - mines.

self.revealed_non_mine_cells: This tracks the number of non-mine cells that have been revealed.

check_win(): This function checks if the number of revealed non-mine cells equals the total non-mine cells. If so, the player has won.

reveal() method: We added self.revealed_non_mine_cells += 1 inside the reveal() method to increment the count of revealed non-mine cells each time the player reveals a valid cell.

play() method: After each move, we check if the player has won by calling self.check_win().

🧪 Example Output
```
0 1 2 3 4 5 6 7 8 9
1
2
3
4
5
6
7
8
9
...
...
0 1 2 3 4 5 6 7 8 9
0
1       1 1 1   1 1 1
2 1 1 1 1 . 1   2 . 2
3 2 . 2 1 1 1   2 . 2
4 2 . 3 1       1 1 1
5 1 2 . 1
6 1 2 2 3 2 1
7 . 1 1 . . 1
8 1 1 2 3 3 1
9     1 . 1
Congratulations! You've won the game.

```
With this fix, the game will correctly detect when the player has won by revealing all the non-mine cells.

## Task 4

### given code 
```
#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)

```
### ChatGPT Degugging :
**See file factorial_recursive.py**

Here's the properly commented and indented version of factorial_recursive.py, with clear documentation for the function including a description, parameters, and return value.

```

#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input integer n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the first command-line argument, convert it to an integer, and compute its factorial

f = factorial(int(sys.argv[1]))
print(f)

```
🔧 Fixes Made
Fixed indentation: The if block was misaligned and would raise an IndentationError.

Added a docstring to factorial() explaining:

What it does.

Its parameter (n) and the type expected.

What it returns, and under which condition.


## Task 5

### given code 
```
class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

```
### ChatGPT Degugging :
**See file checkbook.py**

You're encountering a ValueError because the program tries to convert non-numeric input (like "test") into a float without checking if it's valid. The solution is to wrap the input conversion in a try-except block to catch such errors and prompt the user again.

✅ Changes Made
Wrapped float(input(...)) inside try-except to catch non-numeric values.

Added amount <= 0 check to avoid depositing or withdrawing invalid (e.g., negative) amounts.

Ensured the program does not crash and instead prints a helpful message and continues.

You can now safely test it:

```
bash
$ ./checkbook.py
What would you like to do? (deposit, withdraw, balance, exit): deposit
Enter the amount to deposit: $test
Invalid amount. Please enter a numeric value.
```


## Task 6

### given code 
```
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    print("Player " + player + " wins!")

tic_tac_toe()
```

### ChatGPT Degugging :
**See file tic.py**
Tic Tac Toe implementation is close, but it has several issues, especially in how it:

- Handles game end: The winner message prints the wrong player.

- Does not handle invalid inputs: No checks for out-of-range or non-integer input.

- Doesn't check for a draw: Game can go on forever even when the board is full.

- Could be made cleaner: Some logic like player switching can be simplified.
  
#### 🔧 Fixes and Improvements

| Issue                       | Fix                                                             |
|----------------------------|------------------------------------------------------------------|
| ❌ Wrong winner printed     | Tracked winner and printed the correct one                      |
| ❌ No input validation      | Wrapped input in `try-except`, checked bounds                   |
| ❌ No draw condition        | Added `is_full()` to detect a full board                        |
|  ❌Repeated player switching logic | Replaced with cleaner ternary: `current_player = "O" if ...` |

🧪 Example Game Output
```
   |   |  
-----------
   |   |  
-----------
   |   |  
Enter row (0, 1, or 2) for player X: 0
Enter column (0, 1, or 2) for player X: 0
...
Player X wins!

```
