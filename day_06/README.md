# 🌀 Maze Game (Reeborg’s World)

A simple text-based maze-solving program written in Python, designed for the 'Reeborg’s World' environment.

## 🚀 How it works
- The robot starts at the maze’s entrance.
- The program uses the right-hand rule to navigate:
    - If the right side is clear → turn right and move.
    - Else if the front is clear → move forward.
    - Otherwise → turn left.
- The robot continues until it reaches the goal.


Example:
- Move to the nearest wall.
- Hug the wall on the right side.
- Navigate turns and corridors until the goal is reached.


## 🧠 Concepts Used

- Functions for reusable actions '(turn_right())'
- While loops to repeat actions until the goal is reached
- Conditional statements '(if, elif, else)' for movement logic
- Built-in Reeborg’s World functions:
    - 'move()'
    - 'turn_left()'
    - 'front_is_clear()'
    - 'right_is_clear()'
    - 'at_goal()'

---

## 📁 Project Structure

```
day_06/
│
├── main.py     # Main Python script
└── README.md   # Project description
```

✅ **Day 6 of 100 Days of Code**

🗂️ File: `main.py`

Inspired by the [100 Days of Code](https://www.udemy.com/course/100-days-of-code/) challenge by Angela Yu.
