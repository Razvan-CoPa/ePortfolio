import time
import logging
import json
import os


class BankAcc:
    def __init__(self, owner, IBAN):
        # Attributes/Fields
        self.owner = owner
        self.IBAN = IBAN 
        self.PIN = 0000
        self.sold = 0
        self.active = False
        self.blocked = False
        self.trials = 0
        self.log_file = f'{self.IBAN}.log'
        self.logger = self.setup_logger()        
        self.load_status() 

        if not os.path.exists(f"{self.IBAN}.json"):
            self.log_activity(f"{self.owner}'s account, was created ({self.owner}, {self.IBAN})")                       

    # Methods

    def load_status(self):
        try:
            with open(f"{self.IBAN}.json", "r") as f:
                data = json.load(f)
                self.active = data["active"]
                self.sold = data.get("sold", 0)
                # Load other attributes as needed
        except FileNotFoundError:
            pass


    def save_status(self):
        with open(f"{self.IBAN}.json", "w") as f:
            data = {
                    "active": self.active,
                    "sold": self.sold
                    }
            json.dump(data, f)

    
    def setup_logger(self):
        logger = logging.getLogger(self.IBAN)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
    

    def log_activity(self, message):
        self.logger.info(message)


    def greeting(self):                                                  # Greetings Method
        print(f'Hello {self.owner}!')

    def acc_details(self, user_pin):                                      # Getting account details Method
        if user_pin == self.PIN:
            print(f'Owner: {self.owner}')
            print(f'IBAN: {self.IBAN}')
            print(f'Sold: £{self.sold}')
            print(f'Status(Active): {self.active}')
            print(f'PIN Trials: {self.trials}')
            print('----------------------------')
            self.log_activity(f'{self.owner}, checked bank details.')

        else:
            self.trials +=1
            print("Inccorect PIN")
            self.log_activity(f'{self.owner}, introduced the wrong PIN.')


    def card_activation(self, user_pin):                                  # Activation Method
        if self.active:
            print("Card is already activated.")
            print('----------------------------')
            self.log_activity(f'{self.owner}, tried to activate the card again.') 
            return

        if user_pin == self.PIN:                                          # Correct PIN
            self.greetings()                                              # Greet the customer by calling the "greetings" method
            print('Card successfully activated!')
            print('----------------------------')
            self.active = True
            self.save_status()                                            # Save account status
            self.log_activity(f'{self.owner}, activated their card.')     # Log card activation
            

        elif user_pin != self.PIN:                                        # Incorrect PIN
            self.trials += 1
            if self.trials == 2:                                          # Final attempt
                print('Next wrong PIN will suspend the account!')
                print(f'Attempt: {self.trials}')
                print('--------------------------------------')
                self.log_activity(f'{self.owner}, introduced the wrong PIN 2 times.') 

            elif self.trials > 2:                                         # Exceeded attempts
                print('Your account is now suspended after 3 incorrect PIN attempts!\nPlease visit us in branch to solve the issue.')
                self.log_activity(f'{self.owner}, introduced the wrong PIN more than 3 times.')
                self.blocked = True

            else:                                                         # Incorrect attempts but not final
                print('Incorrect PIN, please try again!')
                print(f'Attempt: {self.trials}')
                print('--------------------------------------')
                self.log_activity(f'{self.owner}, introduced the wrong PIN.')


    def change_pin(self, new_pin):
        if self.active:
            self.PIN = new_pin
            print('PIN successfully changed!')
            self.log_activity(f'{self.owner}, changed the PIN.')
        else:
            print('Cannot change PIN. Please activate your card first.')
            self.log_activity(f'{self.owner}, attempted to changed the PIN.')


    def acc_deposit(self, sum):                                           # Top-up Method
        if self.active and not self.blocked:
            self.sold += sum
            print(f'You successfully deposited the sum of £{sum}.\nYour balance now is: £{self.sold}')
            self.log_activity(f'{self.owner}, added £{sum}. Sold: £{self.sold}.')
            self.save_status()

        else:
            print('Your transaction was declined.\nPlease validate the account/card, prior topping up the account!')
            self.log_activity(f'{self.owner}, attemped to deposit prior activation.')


    def payment(self, sum):                                               # Spend Method
        if sum <= self.sold:
            self.sold -= sum
            print(f'Payment of £{sum}, was successfully made.')
            print(f'Your balance now is: £{self.sold}')
            self.log_activity(f'{self.owner}, spent £{sum}. Sold: £{self.sold}.')
            self.save_status()
        
        else:
            print(f'Insufficient funds!\nBalance: £{self.sold}')
            self.log_activity(f'{self.owner}, attempted to spend £{sum} while sold is £{self.sold}.')

