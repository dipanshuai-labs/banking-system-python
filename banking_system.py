"""
Banking System - Mini Project
AKTU B.Tech CSE | Python Concepts: Variables, Loops, Functions, Dicts, Lists, Modules
"""

import random
import datetime

# ─────────────────────────────────────────────
# DATA STORE (in-memory database using dict)
# ─────────────────────────────────────────────
accounts = {}  # {acc_number: {name, phone, pin, balance, transactions}}

# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def generate_account_number():
    """Generate unique 10-digit account number."""
    while True:
        acc_num = str(random.randint(1000000000, 9999999999))
        if acc_num not in accounts:
            return acc_num

def get_timestamp():
    """Return formatted current date-time."""
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def divider(char="─", width=45):
    print(char * width)

def header(title):
    divider("═")
    print(f"  🏦  {title}")
    divider("═")

def log_transaction(acc_num, txn_type, amount, note=""):
    """Append a transaction record to account history."""
    record = {
        "type": txn_type,
        "amount": amount,
        "timestamp": get_timestamp(),
        "note": note
    }
    accounts[acc_num]["transactions"].append(record)

# ─────────────────────────────────────────────
# FEATURE 1: CREATE ACCOUNT
# ─────────────────────────────────────────────

def create_account():
    header("CREATE NEW ACCOUNT")
    name = input("  Enter your full name    : ").strip()
    if not name:
        print("  ❌ Name cannot be empty.")
        return

    phone = input("  Enter phone number      : ").strip()
    if not phone.isdigit() or len(phone) != 10:
        print("  ❌ Enter a valid 10-digit phone number.")
        return

    pin = input("  Set a 4-digit PIN       : ").strip()
    if not pin.isdigit() or len(pin) != 4:
        print("  ❌ PIN must be exactly 4 digits.")
        return

    confirm_pin = input("  Confirm your PIN        : ").strip()
    if pin != confirm_pin:
        print("  ❌ PINs do not match. Account not created.")
        return

    acc_num = generate_account_number()
    accounts[acc_num] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }

    divider()
    print(f"  ✅ Account Created Successfully!")
    print(f"  👤 Name           : {name}")
    print(f"  📞 Phone          : {phone}")
    print(f"  🔢 Account Number : {acc_num}")
    print(f"  📅 Date           : {get_timestamp()}")
    divider()
    print("  ⚠️  Save your account number safely!\n")

# ─────────────────────────────────────────────
# FEATURE 2: LOGIN
# ─────────────────────────────────────────────

def login():
    header("USER LOGIN")
    acc_num = input("  Enter Account Number : ").strip()
    if acc_num not in accounts:
        print("  ❌ Account not found.\n")
        return

    pin = input("  Enter PIN            : ").strip()
    if accounts[acc_num]["pin"] != pin:
        print("  ❌ Incorrect PIN.\n")
        return

    print(f"\n  ✅ Welcome back, {accounts[acc_num]['name']}!\n")
    account_menu(acc_num)

# ─────────────────────────────────────────────
# FEATURE 3: ACCOUNT MENU
# ─────────────────────────────────────────────

def account_menu(acc_num):
    while True:
        user = accounts[acc_num]
        divider("─")
        print(f"  👤 {user['name']}  |  Acc: {acc_num}")
        divider("─")
        print("  1. Check Balance")
        print("  2. Deposit Money")
        print("  3. Withdraw Money")
        print("  4. Transfer Money")
        print("  5. Transaction History")
        print("  6. Change PIN")
        print("  7. Logout")
        divider("─")

        choice = input("  Select option (1-7) : ").strip()

        if choice == "1":
            check_balance(acc_num)
        elif choice == "2":
            deposit(acc_num)
        elif choice == "3":
            withdraw(acc_num)
        elif choice == "4":
            transfer(acc_num)
        elif choice == "5":
            transaction_history(acc_num)
        elif choice == "6":
            change_pin(acc_num)
        elif choice == "7":
            logout(acc_num)
            break
        else:
            print("  ❌ Invalid option. Try again.\n")

# ─────────────────────────────────────────────
# FEATURE 4: CHECK BALANCE
# ─────────────────────────────────────────────

def check_balance(acc_num):
    balance = accounts[acc_num]["balance"]
    divider()
    print(f"  💰 Current Balance : ₹ {balance:,.2f}")
    print(f"  📅 As of           : {get_timestamp()}")
    divider()

# ─────────────────────────────────────────────
# FEATURE 5: DEPOSIT
# ─────────────────────────────────────────────

def deposit(acc_num):
    header("DEPOSIT MONEY")
    try:
        amount = float(input("  Enter deposit amount (₹) : "))
        if amount <= 0:
            print("  ❌ Amount must be greater than 0.\n")
            return
        accounts[acc_num]["balance"] += amount
        log_transaction(acc_num, "DEPOSIT", amount)
        print(f"  ✅ ₹ {amount:,.2f} deposited successfully!")
        print(f"  💰 New Balance : ₹ {accounts[acc_num]['balance']:,.2f}\n")
    except ValueError:
        print("  ❌ Invalid amount entered.\n")

# ─────────────────────────────────────────────
# FEATURE 6: WITHDRAW
# ─────────────────────────────────────────────

def withdraw(acc_num):
    header("WITHDRAW MONEY")
    try:
        amount = float(input("  Enter withdrawal amount (₹) : "))
        if amount <= 0:
            print("  ❌ Amount must be greater than 0.\n")
            return
        if amount > accounts[acc_num]["balance"]:
            print("  ❌ Insufficient balance.\n")
            return
        accounts[acc_num]["balance"] -= amount
        log_transaction(acc_num, "WITHDRAW", amount)
        print(f"  ✅ ₹ {amount:,.2f} withdrawn successfully!")
        print(f"  💰 New Balance : ₹ {accounts[acc_num]['balance']:,.2f}\n")
    except ValueError:
        print("  ❌ Invalid amount entered.\n")

# ─────────────────────────────────────────────
# FEATURE 7: TRANSFER
# ─────────────────────────────────────────────

def transfer(acc_num):
    header("TRANSFER MONEY")
    receiver = input("  Enter receiver's account number : ").strip()

    if receiver == acc_num:
        print("  ❌ Cannot transfer to your own account.\n")
        return
    if receiver not in accounts:
        print("  ❌ Receiver account not found.\n")
        return

    try:
        amount = float(input("  Enter transfer amount (₹)       : "))
        if amount <= 0:
            print("  ❌ Amount must be greater than 0.\n")
            return
        if amount > accounts[acc_num]["balance"]:
            print("  ❌ Insufficient balance.\n")
            return

        accounts[acc_num]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        note_sender = f"Transferred to {accounts[receiver]['name']} (Acc: {receiver})"
        note_receiver = f"Received from {accounts[acc_num]['name']} (Acc: {acc_num})"

        log_transaction(acc_num, "TRANSFER OUT", amount, note_sender)
        log_transaction(receiver, "TRANSFER IN", amount, note_receiver)

        print(f"  ✅ ₹ {amount:,.2f} transferred to {accounts[receiver]['name']}!")
        print(f"  💰 Your Balance : ₹ {accounts[acc_num]['balance']:,.2f}\n")
    except ValueError:
        print("  ❌ Invalid amount entered.\n")

# ─────────────────────────────────────────────
# FEATURE 8: TRANSACTION HISTORY
# ─────────────────────────────────────────────

def transaction_history(acc_num):
    header("TRANSACTION HISTORY")
    txns = accounts[acc_num]["transactions"]

    if not txns:
        print("  📭 No transactions yet.\n")
        return

    print(f"  {'#':<4} {'Type':<14} {'Amount (₹)':>12}  {'Date & Time':<20}")
    divider()
    for i, txn in enumerate(txns, 1):
        note = f"  → {txn['note']}" if txn["note"] else ""
        print(f"  {i:<4} {txn['type']:<14} {txn['amount']:>12,.2f}  {txn['timestamp']}")
        if note:
            print(f"       {note}")
    divider()
    print(f"  Total Transactions : {len(txns)}\n")

# ─────────────────────────────────────────────
# FEATURE 9: CHANGE PIN
# ─────────────────────────────────────────────

def change_pin(acc_num):
    header("CHANGE PIN")
    old_pin = input("  Enter current PIN  : ").strip()
    if old_pin != accounts[acc_num]["pin"]:
        print("  ❌ Incorrect current PIN.\n")
        return

    new_pin = input("  Enter new 4-digit PIN : ").strip()
    if not new_pin.isdigit() or len(new_pin) != 4:
        print("  ❌ PIN must be exactly 4 digits.\n")
        return

    confirm = input("  Confirm new PIN    : ").strip()
    if new_pin != confirm:
        print("  ❌ PINs do not match.\n")
        return

    accounts[acc_num]["pin"] = new_pin
    print("  ✅ PIN changed successfully!\n")

# ─────────────────────────────────────────────
# FEATURE 10: LOGOUT
# ─────────────────────────────────────────────

def logout(acc_num):
    print(f"\n  👋 Logged out successfully. Goodbye, {accounts[acc_num]['name']}!\n")

# ─────────────────────────────────────────────
# MAIN MENU
# ─────────────────────────────────────────────

def main():
    while True:
        header("PYTHON BANKING SYSTEM")
        print("  1. Create New Account")
        print("  2. Login to Account")
        print("  3. Exit")
        divider("═")
        choice = input("  Select option (1-3) : ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\n  🏦 Thank you for using Python Banking System. Goodbye!\n")
            break
        else:
            print("  ❌ Invalid option. Please try again.\n")

# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
