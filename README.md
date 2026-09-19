# 🏦 Python Banking System – Mini Project

**AKTU B.Tech CSE | Python Mini Project | Session 2022–2026**

---

## 📌 Project Overview

A Python-based CLI banking application simulating real-world banking operations — account creation, secure login, deposits, withdrawals, transfers, and transaction history.

---

## 🚀 Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | Create Account | Name, Phone, PIN → Auto-generate Account Number |
| 2 | Login | Account Number + PIN authentication |
| 3 | Check Balance | View current balance with timestamp |
| 4 | Deposit | Add funds to account |
| 5 | Withdraw | Deduct funds with balance validation |
| 6 | Transfer | Send money to another account |
| 7 | Transaction History | View all past transactions |
| 8 | Change PIN | Secure PIN update with confirmation |
| 9 | Logout | End session, return to main menu |

---

## 🐍 Python Concepts Used

- **Variables & Data Types** — strings, floats, integers
- **Conditional Statements** — if/elif/else for validation
- **Loops** — while loop for menu navigation
- **Functions** — modular design, one function per feature
- **Lists & Dictionaries** — account data store + transaction history
- **String Operations** — formatting, `.strip()`, `.isdigit()`
- **Modules** — `random` (account number), `datetime` (timestamps)

---

## 📁 Project Structure

```
banking_system/
│
├── banking_system.py   ← Main project file
└── README.md           ← Project documentation
```

---

## ▶️ How to Run

```bash
python banking_system.py
```

> No external libraries required. Runs on Python 3.x.

---

## 📊 Flow

```
MAIN MENU
 ├── Create Account → Generate Acc No + Set PIN
 └── Login → Account No + PIN
              └── ACCOUNT MENU
                   ├── Check Balance
                   ├── Deposit
                   ├── Withdraw
                   ├── Transfer
                   ├── Transaction History
                   ├── Change PIN
                   └── Logout → MAIN MENU
```

---

## 👤 Author

**Dipanshu**  
B.Tech CSE | H.R. Institute of Technology, Ghaziabad  
AKTU | Session 2022–2026
