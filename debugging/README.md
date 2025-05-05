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
**See file factorial_recursive.py **

``````
