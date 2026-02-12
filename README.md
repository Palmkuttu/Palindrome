# Palindrome Validator (Assignment 4)

**Name:** Dennis Zacharia  
**Date:** February 12, 2026  
**Course/Assignment:** Assignment 4 — Palindrome (Deque + TDD)

## Overview
This project validates whether a given input string is a **palindrome** (reads the same forward and backward), using a **`deque`** for efficient pops from both ends.  
✅ **No `reverse()` / slicing `[::-1]` / sorting** is used.

## Requirements Met
- `palindrome.py` contains a function **`is_palindrome(value)`**
- Function accepts **one parameter**
- Returns **True** or **False**
- Uses a **deque** to compare characters from both ends
- Tests are written in **`test_palindrome.py`**
- Tests run locally with **pytest** and on **GitHub Actions**

## Rules Used for Checking
- Only **letters and numbers** are considered
- Spaces and punctuation are ignored
- Comparison is **case-insensitive**
- If input is **not a string**, the function raises **ValueError**
- Empty string (`""`) returns **False** (as required by tests)

## How to Run Locally

### 1) Create/activate virtual environment (optional)
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
