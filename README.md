# Library-Management-System-Python
# 📚 Library Management System

A menu-driven **Library Management System** developed in Python using **Object-Oriented Programming (OOP)**. This mini project demonstrates fundamental Python programming concepts including classes, objects, constructors, methods, conditional statements, loops, functions, data structures, exception handling, and CSV file handling.

## ✨ Features

* ➕ Add new books
* 📖 View all books
* 🔍 Search books by ID, title, author, or category
* 📤 Issue books to students
* 📥 Return books
* 🗑️ Remove books
* 📂 View available book categories
* 📋 View currently issued books
* 📊 View library statistics
* 💾 Automatically store book records in a CSV file
* ⚠️ Gracefully handle invalid user input and errors

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming**
* **CSV File Handling**
* **Exception Handling**

## 🧠 Python Concepts Demonstrated

This project demonstrates concepts learned during Week 1:

* Variables
* Input and output
* Conditional statements (`if`, `elif`, `else`)
* `for` loops
* `while` loops
* Functions
* Classes and objects
* Constructors (`__init__`)
* Methods
* Lists
* Sets
* Dictionaries
* List comprehensions
* String manipulation
* Exception handling
* File handling
* CSV data storage

## 🏗️ Classes

### `Book`

The `Book` class represents an individual book and stores:

* Book ID
* Book title
* Author
* Category
* Issue status
* Student to whom the book is issued

It also contains methods for:

* Issuing a book
* Returning a book

### `Library`

The `Library` class manages the complete library system.

It handles:

* Adding books
* Displaying books
* Searching books
* Issuing and returning books
* Removing books
* Managing categories
* Displaying statistics
* Reading and writing CSV data

## 📁 Project Structure

```text
Library-Management-System-Python/
│
├── library_management.py
├── library_books.csv
└── README.md
```

### `library_management.py`

Contains the complete Python application.

### `library_books.csv`

Stores the library's book records. The program automatically updates this file whenever books are added, issued, returned, or removed.

### `README.md`

Contains the documentation and information about the project.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project in VS Code

Open the downloaded project folder in Visual Studio Code.

### 3. Run the program

Open the VS Code terminal and execute:

```bash
python library_management.py
```

## 📋 Application Menu

```text
=======================================================
        LIBRARY MANAGEMENT SYSTEM
=======================================================
1. Add New Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Remove Book
7. View Book Categories
8. View Issued Books
9. Library Statistics
10. Exit
=======================================================
```

## 💾 Data Storage

The application uses a CSV file named `library_books.csv` to permanently store book information.

The stored fields are:

```text
book_id
title
author
category
is_issued
issued_to
```

This means that the data remains available even after the program is closed and restarted.

## ⚠️ Error Handling

The application uses Python's `try-except` mechanism to handle invalid input and file-related errors.

For example, if a user enters text instead of a menu number, the program displays an appropriate error message instead of crashing.

## 🎯 Project Objective

The objective of this project is to create a practical Python application that combines **Object-Oriented Programming with fundamental Python concepts** in a single menu-driven system.

It demonstrates how real-world problems can be solved by organizing data and functionality into classes, objects, methods, and reusable functions.

## 🚀 Future Enhancements

The project can be extended with:

* Student/member registration
* Due dates for issued books
* Late return fines
* Login and authentication
* Admin and student accounts
* Book availability notifications
* Sorting and filtering
* Advanced reports
* SQLite/MySQL database integration
* Graphical User Interface (GUI)

## 👩‍💻 Project Type

**Python Mini Project – Object-Oriented Programming (OOP)**

---

⭐ If you found this project useful, consider giving the repository a star!

