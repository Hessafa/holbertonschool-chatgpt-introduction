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


