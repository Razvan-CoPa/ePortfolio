## BankAccount Class Implementation

This Python script implements a simple BankAccount class that allows users to create and manage a bank account. The class provides functionality to activate the account, manage the PIN, deposit money, make payments, and more. It also includes features such as account locking after multiple failed login attempts, age verification, and activity logging.

### Features

Account Creation: Users can create a bank account with a unique account number, account holder name, and date of birth. Age validation ensures that users are at least 18 years old to open an account.

PIN Management: The account starts with a PIN set to the user's year of birth, and users can change their PIN after activation. Incorrect PIN entries trigger account locking after three failed attempts, and the account is locked for 5 minutes.

Account Activation: The account is inactive by default. The user must activate the account by changing the default PIN.

Deposits and Payments: Users can deposit money into their account and make payments. Payments are restricted by the available balance.

Activity Logging: All activities are logged with timestamps, such as PIN changes, deposits, payments, and login attempts.

Account File Storage: Account details are stored in a JSON file, and account activities are logged in a separate text file.

### Requirements
Python 3.x
No external libraries required

How It Works
Create a Bank Account: To create a bank account, you need to provide the account number, account holder's name, and date of birth.

Account Activation: The account is initially inactive, and the PIN is set to the year of birth. To activate the account, the user must change the PIN.

Login: The user can log in using the correct PIN. After three failed login attempts, the account will be locked for 5 minutes.

Deposit and Payment: Once the account is active, users can deposit funds and make payments from the account. A payment will only be allowed if there are sufficient funds.

Saving and Loading Data: Account details are saved in a file, and the account will load its details when reinitialized, preserving the balance, PIN, and activation status.

### Methods
1. __init__(account_number, account_holder, date_of_birth)
Constructor that initializes the account with the given account number, account holder name, and date of birth.

Parameters:

account_number: Unique identifier for the account.

account_holder: Name of the account holder.

date_of_birth: Date of birth in YYYY-MM-DD format.

2. calculate_age(date_of_birth)
Calculates the age of the account holder based on their date of birth.

Returns: The age of the account holder.

3. load_account()
Loads the account's data (balance, PIN, active status) from a JSON file.

Returns: None

4. save_account()
Saves the current account details (balance, PIN, active status) to a JSON file.

Returns: None

5. log_activity(activity)
Logs a specific activity in the account's activity log file with a timestamp.

Parameters: activity (str) – The activity to log.

Returns: None

6. card_activation()
Activates the account by prompting the user to change the PIN from the default (year of birth).

Returns: None

7. greeting()
Prints a greeting message with the account holder's name.

Returns: None

8. login(entered_pin)
Attempts to log in with the provided PIN. If incorrect, the account will be locked after three failed attempts for 5 minutes.

Parameters: entered_pin (str) – The PIN entered by the user.

Returns: True if login is successful, False if login fails or account is locked.

9. change_pin(old_pin, new_pin)
Allows the user to change the PIN if the current PIN matches the old one, and the account is active and unlocked.

Parameters:

old_pin: The current PIN to verify.

new_pin: The new PIN to set.

Returns: True if PIN is changed successfully, False otherwise.

10. acc_deposit(amount, entered_pin)
Deposits a specified amount into the account if the account is active, the PIN is correct, and the amount is positive.

Parameters:

amount: The amount to deposit.

entered_pin: The PIN entered by the user.

Returns: True if the deposit is successful, False otherwise.

11. payment(amount, entered_pin)
Makes a payment from the account if the account is active, the PIN is correct, there are sufficient funds, and the amount is positive.

Parameters:

amount: The amount to pay.

entered_pin: The PIN entered by the user.

Returns: True if the payment is successful, False otherwise.

### Example Usage
# Create a new BankAccount object
account = BankAccount(account_number="123456789", account_holder="John Doe", date_of_birth="1990-01-01")

# Load account data
account.load_account()

# Activate the card
account.card_activation()

# Login with the correct PIN
account.login("1990")

# Deposit money
account.acc_deposit(1000, "1990")

# Make a payment
account.payment(200, "1990")

# Change the PIN
account.change_pin("1990", "2020")
File Structure
BankAccount.py: The script containing the BankAccount class.

{account_number}_account.json: A JSON file storing account data (balance, PIN, activation status).

{account_number}_activity.log: A log file storing activities (e.g., login attempts, PIN changes, deposits, and payments).

### Future Improvements
Add more sophisticated security features, like multi-factor authentication.
Support for multiple accounts and account types (e.g., savings, checking).
Integrate with a database for persistent storage rather than relying on file-based storage.