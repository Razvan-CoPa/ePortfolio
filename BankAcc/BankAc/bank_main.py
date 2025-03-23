from bank_acc import BankAccount
from datetime import datetime

# Calculate date of birth from age (assuming the person is 27 years old and the current date is March 23, 2025)
age = 27
current_year = datetime.now().year
birth_year = current_year - age
date_of_birth = f"{birth_year}-03-23"  # Adjust birthdate to match the correct format

# Create an account (should succeed if age >= 18)
try:
    account = BankAccount("GB0001", "Razvan", date_of_birth)  # Pass date_of_birth as a string
    print("\n✅ Account created successfully.")
except ValueError as e:
    print(f"\n❌ {e}")

# Activate account
print("\n--- Activating Account ---")
account.card_activation()  # Should activate the account
account.card_activation()  # Should say it's already activated

# Set a PIN (initial setup)
account.pin = "1234"
account.save_account()

# Attempt login (only correct PIN, avoiding lock)
print("\n--- Login Attempts ---")
account.login("1234")  # Correct PIN, should succeed

# Change PIN (wrong old PIN first, then correct)
print("\n--- Changing PIN ---")
account.change_pin("0000", "5678")  # Wrong old PIN, should fail
account.change_pin("1234", "5678")  # Correct PIN, should succeed

# Deposit money (correct PIN)
print("\n--- Depositing Money ---")
account.acc_deposit(100, "5678")  # Correct PIN

# Spend money (correct PIN, including insufficient funds check)
print("\n--- Spending Money ---")
account.payment(50, "5678")  # Should succeed
account.payment(100, "5678")  # Should fail (insufficient funds)

# Check log file
print("\n✅ All tests completed. Check the log file for details.")
