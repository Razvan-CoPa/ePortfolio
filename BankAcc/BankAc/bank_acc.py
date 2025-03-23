import time
import json
import os
from datetime import datetime

class BankAccount:
    def __init__(self, account_number, account_holder, date_of_birth):
        if isinstance(date_of_birth, int):  
            self.date_of_birth = datetime(year=date_of_birth, month=1, day=1)
        else:
            self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
            self.age = self.calculate_age(self.date_of_birth)

        if self.age < 18:
            raise ValueError("❌You must be at least 18 years old to open an account.")
        
        self.account_number = account_number
        self.account_holder = account_holder
        self.pin = str(self.date_of_birth.year)  # Initial PIN is user's year of birth
        self.balance = 0.0
        self.active = False
        self.failed_attempts = 0
        self.locked_until = 0  # Time until the account is unlocked
        self.cooldown_time = 5 * 60  # Cooldown period of 5 minutes in seconds
        self.script_directory = os.path.dirname(os.path.abspath(__file__))


    # Helper method to get the file path
    def get_file_path(self, filename):
        return os.path.join(self.script_directory, filename)
    


    def calculate_age(self, date_of_birth):
        today = datetime.today()
        return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    


    def load_account(self):
        account_file = self.get_file_path(f"{self.account_number}_account.json")
        
        # Check if the file exists
        if os.path.exists(account_file):
            try:
                with open(account_file, "r") as file:
                    data = json.load(file)
                    self.balance = data["balance"]
                    self.pin = data["pin"]
                    self.active = data["active"]
                    print("Account loaded successfully.")
            except json.JSONDecodeError:
                print("❌ Error loading account data. File may be corrupted.")
        else:
            print("⚠️ Account file not found. A new account will be created.")
            # Save account with default values if no file is found
            self.save_account() 
    



    def save_account(self):
        account_file = self.get_file_path(f"{self.account_number}_account.json")
        data = {
            "balance": self.balance,
            "pin": self.pin,
            "active": self.active
        }
        
        # Create or update the account file
        with open(account_file, "w") as file:
            json.dump(data, file)
            print("✅ Account data saved successfully.")




    def log_activity(self, activity):
        log_file = self.get_file_path(f"{self.account_number}_activity.log")
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {activity}\n"
        
        with open(log_file, "a") as file:
            file.write(log_entry)
        
        print(f"📌 Log: {activity}")




    def card_activation(self):
        if not self.active:
            if self.pin == str(self.date_of_birth.year):
                print(f"❌ Your account PIN is still set to your year of birth. Please change it for security reasons.")
                return False
            
            self.active = True
            self.save_account()
            self.log_activity(f"{self.account_holder}, activated their card.")
            print("✅ Your card has been activated.")
        else:
            print("⚠️ Your card is already activated.")

    


    def greeting(self):
        print(f"Hello, {self.account_holder}!")




    def login(self, entered_pin):
        if self.locked_until > time.time():
            remaining_lock_time = int(self.locked_until - time.time())
            print(f"❌ Account is locked. Try again after {remaining_lock_time} seconds.")
            return False
        if self.pin == entered_pin:
            self.failed_attempts = 0  # Reset failed attempts after successful login
            print("✅ Login successful!")
            return True
        else:
            self.failed_attempts += 1
            self.log_activity(f"{self.account_holder}, introduced the wrong PIN.")
            if self.failed_attempts >= 3:
                self.locked_until = time.time() + self.cooldown_time
                print("❌ Account locked due to too many failed attempts. Try again later.")
            else:
                print("❌ Incorrect PIN. Try again.")
            return False
        



    def change_pin(self, old_pin, new_pin):
        if not self.active:
            print("❌ Cannot change PIN. Your account is not activated.")
            return False

        if self.locked_until > time.time():
            print("❌ Account is locked. You cannot change the PIN until the account is unlocked.")
            return False
        
        if self.pin == old_pin:
            self.pin = new_pin
            self.save_account()
            self.log_activity(f"{self.account_holder}, changed the PIN.")
            print("✅ PIN changed successfully!")
            return True
        else:
            print("❌ Incorrect PIN. PIN change failed.")
            return False
        



    def acc_deposit(self, amount, entered_pin):
        if not self.active:
            self.log_activity(f"{self.account_holder}, attempted to top-up the account.")
            print("❌ Cannot deposit money. Your account is not activated.")
            return False
        
        if self.pin != entered_pin:
            print("❌ Incorrect PIN. Cannot deposit money.")
            return False

        if amount < 0:
            self.log_activity(f"{self.account_holder}, attempted to top-up the account with negative amount.")
            print("❌ Cannot deposit a negative amount.")
            return False

        self.balance += amount
        self.save_account()
        self.log_activity(f"{self.account_holder}, added {amount}. Sold: {self.balance}.")
        print(f"✅ Deposited £{amount}. New balance is £{self.balance}.")
        return True
    



    def payment(self, amount, entered_pin):
        if not self.active:
            print("❌ Cannot make a payment. Your account is not activated.")
            return False
        
        if self.pin != entered_pin:
            print("❌ Incorrect PIN. Cannot make a payment.")
            return False

        if amount < 0:
            print("❌ Cannot make a payment of a negative amount.")
            return False
        if amount > self.balance:
            self.log_activity(f"{self.account_holder}, attempted to spend {amount} while sold is {self.balance}.")
            print(f"❌ Insufficient balance: £{self.balance}")
            return False

        self.balance -= amount
        self.save_account()
        self.log_activity(f"{self.account_holder}, spent {amount}. Sold: {self.balance}.")
        print(f"✅ Payment of £{amount} made. New balance is £{self.balance}.")
        return True