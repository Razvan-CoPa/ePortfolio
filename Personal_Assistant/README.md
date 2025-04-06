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
add	Add a new contact
delete	Delete an existing contact
edit	Edit contact's phone or email
birthday	Add or update a contact's birthday
phone	Get the phone number of a contact
email	Get the email of a contact
show all	Display all saved contacts
search	Search contacts by name
note add	Add a note
note show	Display all notes
note delete	Delete a specific note
address add	Add an address with a name
address show	Show all saved addresses
address delete	Delete a specific address
birthdays	Show upcoming birthdays
help	Show command list
exit, quit	Exit the assistant
### File Structure
bash
Copy
Edit
personal-assistant/
│
├── personal_assistant.py      # Main application script
├── data.pkl                   # Auto-generated file to persist data
└── README.md                  # Project documentation
### Future Improvements
📅 Calendar or event reminders

🔒 Encrypted storage for sensitive information

📤 CSV/JSON import/export support

🌦️ Weather integration for stored addresses

🗣️ Voice input and speech feedback

### Author
Developed with ❤️ by Razvan Paraschiva
Inspired by the idea of a smart yet minimal digital assistant.