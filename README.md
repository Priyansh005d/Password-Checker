# Password Verification Script 🔐

This is a simple Python script that verifies a user-entered password by checking it against a saved password in a local text file (`password.txt`).

## 📁 Files

- `main.py`: The main script that prompts the user to enter a password and verifies it.
- `password.txt`: A text file that contains the correct password (stored in plain text for simplicity).

## 🛠 How It Works

1. The user is prompted to enter a password.
2. The script reads the password from `password.txt`.
3. It compares the entered password with the one in the file.
4. If they match, access is granted. If not, access is denied.

## ✅ Sample Output

```bash
Enter your Password: ••••••••
Correct Password
You may proceed further...

or
Enter your Password: ********
Incorrect password
Access Denied
