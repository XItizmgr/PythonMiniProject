# Python Mini-Projects Collection

A curated collection of simple, functional Python applications ranging from utility tools to basic AI and data management scripts. Built as part of my Python learning journey.

---

## Repository Structure

This repository contains the following independent mini-projects:

*   **`Fake_News_generator/`** – A Python script using basic text processing
*   **`Student_result_manager/`** – A data management tool that tracks student scores and records using JSON persistence.
*   **`Password_generator/`** – A security utility that generates random, secure passwords and saves them locally.
*   **`Siimple_calculator/`** – A terminal-based calculator featuring arithmetic operations and a session history log.


---

## Projects Overview

### 1. Fake News Generator
*   **File:** `Fake_News_generator/main.py`
*   **Description:** Generates or processes text headlines to simulate fake news patterns.

### 2. Student Result Manager
*   **Files:** `Student_result_manager/main.py`, `student.json`
*   **Description:** Allows adding, viewing, and managing student grades. Uses a native JSON structure to ensure records are saved even after the program closes.

### 3. Password Generator
*   **Files:** `Password_generator/main..py`, `password.txt`
*   **Description:** Generates strong, highly customizable passwords based on user-defined lengths. It automatically exports generated options to a local text file for easy access.

### 4. Simple Calculator
*   **Files:** `Siimple_calculator/calculator.py`, `history.txt`
*   **Description:** Evaluates mathematical expressions smoothly and appends a detailed calculation log to a history file.

---

## Setup & How to Run

### Prerequisites
Make sure you have **Python 3.x** installed on your system. 

### Running a Project
Since each project lives in its own subdirectory, navigate to the specific folder and execute the main Python file. For example, to run the **Student Result Manager**:

```bash
# Navigate to the project directory
cd Student_result_manager

# Run the application
python main.py
