# 🔐 PyPassword Generator

A simple, text-based password generator that creates a secure password based on the number of letters, numbers, and symbols specified by the user.

## 🚀 How it works
1. The program prompts the user to input how many letters, symbols, and numbers they want in their password.
2. It randomly selects characters from predefined lists of letters, numbers, and symbols according to the user's input.
3. The selected characters are shuffled to enhance password randomness and strength.
4. The final password is displayed to the user.


Example:
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
3
How many numbers would you like?
2
Here is your password: %e9%4#UVI


## 🧠 Concepts Used

- User input via input()
- Random selection using Python’s random module
- Lists for storing characters (letters, numbers, symbols)
- Looping through user-defined ranges
- Shuffling a list to randomize password structure
- and again looping through to make the password stronger via suffle

---

## 📁 Project Structure

```
day_05/
│
├── main.py     # Main Python script
└── README.md   # Project description
```

✅ **Day 5 of 100 Days of Code**

🗂️ File: `main.py`

Inspired by the [100 Days of Code](https://www.udemy.com/course/100-days-of-code/) challenge by Angela Yu.
