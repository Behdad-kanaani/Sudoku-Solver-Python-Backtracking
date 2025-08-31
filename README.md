# Sudoku Solver - Backtracking Algorithm in Python

[![GPLv3 License](https://img.shields.io/badge/license-GPLv3-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Issues](https://img.shields.io/github/issues/Behdad-kanaani/Sudoku-Solver-Python-Backtracking)](https://github.com/Behdad-kanaani/Sudoku-Solver-Python-Backtracking/issues)
[![Stars](https://img.shields.io/github/stars/Behdad-kanaani/Sudoku-Solver-Python-Backtracking?style=social)](https://github.com/Behdad-kanaani/Sudoku-Solver-Python-Backtracking/stargazers)

---

## 📘 Description

This is a **Sudoku Solver** implemented in Python using the **Backtracking algorithm**. It reads a 9×9 Sudoku grid with empty cells represented as `"."` and fills it with a valid solution — if one exists — using depth-first search and constraint checking.

The algorithm is fast, clean, and easy to follow, making it a great learning resource for:
- Recursion
- Backtracking
- Constraint Satisfaction Problems (CSP)

---

## 🎯 Features

- 🧠 Solves any valid 9×9 Sudoku puzzle
- 🔁 Implements efficient backtracking with pruning
- 📦 Pure Python, no external dependencies
- 📚 Clean and well-commented code
- 🖨️ Nicely formatted terminal output

---

## ⚙️ How It Works

1. **Board Parsing**:
   - Identifies all empty cells
   - Tracks which digits are already used in each row, column, and 3×3 box

2. **Backtracking Algorithm**:
   - For each empty cell, tries digits from 1 to 9
   - If a digit is valid, it is placed, and the solver proceeds to the next cell
   - If no valid digit is found, it backtracks and tries another digit

3. **Recursive Solution**:
   - Uses a depth-first search approach to fill the board completely

---

## ✅ Prerequisites

- Python 3.x installed  
- Terminal / Command Line access

---

## 🚀 Installation & Usage

### Clone the repository:

```bash
git clone https://github.com/Behdad-kanaani/Sudoku-Solver-Python-Backtracking.git
cd Sudoku-Solver-Python-Backtracking
````

### Run the solver:

```bash
python main.py
```

---

## 🧪 Example

### 🔹 Input Board

```
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9
```

### ✅ Solved Board

```
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

---

## 📁 Project Structure

```
📦 Sudoku-Solver-Python-Backtracking
├── main.py     # Main script with solver logic
└── README.md            # Project documentation
```

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

---

## 👨‍💻 Author

* **Behdad Kanaani**
  [🔗 GitHub](https://github.com/Behdad-kanaani)

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

You may copy, distribute, and/or modify this software under the terms of the GPL.
See the [LICENSE](LICENSE) file for full license details.

---

## 🌟 Star this repo if you found it useful!
