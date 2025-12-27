# 🧮 Calcify – Simple Calculator (Python)

**Calcify** is a console-based calculator application built using Python.  
It evaluates full mathematical expressions entered by the user and supports continuous calculations until the user exits.

---

## 🚀 Features

- ➕ Addition (`+`)
- ➖ Subtraction (`-`)
- ✖️ Multiplication (`*`)
- ➗ Division (`/`)
- 🧠 Accepts full expressions (e.g. `1+2*3-4/5`)
- 🚫 Handles division by zero errors
- 🔒 Allows only numbers and valid operators
- 🔁 Runs continuously until user types **`exit`**

---

## 🛠️ Technologies Used

- **Language:** Python  
- **Concepts Applied:**
  - Functions
  - Loops
  - Exception Handling
  - Input Validation
  - `eval()` function

---

## 📂 Project Structure

Calcify/
│
├── calcify.py
└── README.md

yaml
Copy code

---

## ▶️ How to Run the Program

### Prerequisites
- Python **3.x** installed

### Steps
1. Clone or download the repository
2. Open terminal / command prompt
3. Navigate to the project directory
4. Run the program:

```bash
python calcify.py
📝 Example Usage
vbnet
Copy code
==== Welcome to Calcify-Simple Calculator ===
Supports : Addtion(+), Subtraction(-), Multiplication(*), Division(/)
Type 'exit' to quit.

Enter Expression: 1+2*3
Result: 7

Enter Expression: 10/0
Error : Division by Zero

Enter Expression: exit
Exiting Calcify
🧠 How It Works
User inputs a mathematical expression

Program validates characters (numbers & operators only)

Expression is evaluated using eval()

Errors are handled using try-except

Loop continues until user types exit

⚠️ Limitations
Uses eval() (safe only due to strict character filtering)

No scientific operations (sin, cos, power, etc.)

Console-based only

🔮 Future Enhancements
Replace eval() with a custom parser

Add scientific calculator features

Add GUI using Tkinter

Add calculation history

Improve expression validation

👨‍💻 Author
Name: Jahid

Course: BTech CSE (AI Specialization)

Purpose: Python mini project for logic building and exception handling

⭐ Support
If you like this project, give it a ⭐ on GitHub!

yaml
Copy code

---

### ⚠️ Small Code Fix Recommendation (Important)
In your code, change:
```python
except exception as e:
to:

python
Copy code
except Exception as e:
