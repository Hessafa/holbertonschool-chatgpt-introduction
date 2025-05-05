# holbertonschool-chatgpt-introduction
This Project is for Enhancing Code Quality and Efficiency with ChatGPT- Debugging
## Task 0 
given code 
```

ChatGPT Degugging :
The issue in your factorial.py script is that the while loop never updates the value of n, which results in an infinite loop. You're multiplying result *= n repeatedly, but since n never decreases, the condition n > 1 is always true.

✅ Fix
You need to decrement n inside the loop
see the file factorial.py
🧪 Example Output
```bash
$ ./factorial.py 5
120

$ ./factorial.py 0
1
This fixed version correctly computes the factorial by decrementing n in each iteration.
```
## Task 1
ChatGPT Debugging :

