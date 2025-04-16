
# Number Guessing Game (Binary Search Edition)

This is a simple Python console game where the **computer guesses the number you're thinking of** using a binary search strategy.

## 🧠 How It Works

1. You provide a **lower** and **upper bound**.
2. Think of a number within that range (inclusive).
3. The computer will guess your number, and you respond with:
   - `'='` if the guess is correct
   - `'>'` if your number is higher
   - `'<'` if your number is lower
4. The computer will guess your number in **log₂(n)** attempts or fewer — assuming you play fair!

## 🛠 How to Run

Make sure you have Python 3 installed, then run:

```bash
python3 guess_number.py
