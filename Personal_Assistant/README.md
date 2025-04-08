## Personal Assistant CLI (Python)
A lightweight, command-line personal assistant built with Python. It allows you to manage your contacts, notes, birthdays, and addresses—all stored locally with persistent storage using pickle.

### Features
👤 Add, view, edit, and delete contacts with phone numbers, emails, and birthdays

📝 Create and manage notes

🎂 Birthday reminder functionality

🏠 Store addresses associated with names

💾 Automatic saving and loading of data on launch/exit

### Tech Stack
Python 3.7+

Built-in libraries: pickle, datetime, re

### Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/personal-assistant-cli.git
cd personal-assistant-cli
2. Run the script
bash
Copy
Edit
python personal_assistant.py
### Available Commands
Once you're inside the CLI, you can use the following commands:

Command	Description

add ___             - To add a new contact, (name and number)

edit ___            - To edit an existing contact's number, (name + new number)

edit-name ___       - To edit the name of an existing contact, (old name + new name)

add-address ___     - To add an address for an existing contact, (contact name  + house number, street, city, country)

edit-address ___    - To edit the address of a contact, (contact name + new address)

show ___            - To display a specific contact,

contacts            - To display all contacts,

add-email ___       - To add an email address to an existing contact, (this command can also change the current email),

add-birthday ___    - To add birthday to an existing contact, (DD/MM/YYYY)

delete ___          - To delete a contact,

clear_all           - To delete all contacts,

show-birthday ___   - To display the birthday of a contact,

birthdays           - To display the birthdays of contacts occurring in the next week,

add-note ___        - To start writing your note, (note ID + your text)

edit-note ___       - To edit an existing note, (note ID + new text)

notes               - To display all notes,

delete-note ___     - To delete an existing note, (note ID),

search-note___      - To find a specific note by a keyword, (keyword)

And "exit" or "close"

### Future Improvements
📅 Calendar or event reminders

🔒 Encrypted storage for sensitive information

📤 CSV/JSON import/export support

🌦️ Weather integration for stored addresses

🗣️ Voice input and speech feedback

### Author
Developed with ❤️ by Razvan Paraschiva, inspired by the idea of a smart yet minimal digital assistant.