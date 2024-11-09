# Voice-Activated-Transactions

Project Overview
The Voice-Activated UPI Transaction System is an innovative solution designed to streamline UPI transactions using voice commands. Built with Python, Streamlit, and SQLite, this project demonstrates a simple yet effective approach to conducting secure transactions through voice recognition. It includes essential functionalities like user login, transaction processing, balance management, and account handling, all accessible via a user-friendly interface.

This application is ideal for those looking to explore the integration of voice commands with financial technology in a localized setup. The project is developed as a local application and uses Python libraries to simulate a complete transaction flow.

Features
1. Secure Login System
Users log in with a predefined username and password.
Credentials are validated against an SQLite database, ensuring secure access to accounts.
Displays the user’s balance upon login.
2. Voice-Activated Transactions
Users can record a voice command to initiate transactions.
The recorded audio is transcribed into text, parsed for the transaction amount and recipient name.
The system validates recipient information, ensuring the receiver exists in the database.
If the recipient is valid, the amount is deducted from the sender's balance and credited to the receiver.
Shows “Balance Before Transaction” and “Balance After Transaction” separately, offering clarity on financial changes.
3. Add/Delete User
Users can add new accounts, providing a username, password, and initial balance.
Each new user entry is added to the database and can later be removed through account management.
Allows for dynamic user management within a localized database structure.
4. Interactive Frontend with Streamlit
Streamlit provides an interactive, easy-to-use UI where users can:
Log in and view balances.
Initiate transactions via voice recording.
Add or delete users from the system.
View transaction success messages and balance updates in real-time.
System Requirements
Software
Python 3.8 or higher
Streamlit for the frontend interface
SQLite for the database backend
SpeechRecognition and other libraries (optional for real voice-to-text integration)
Python Libraries
streamlit
sqlite3 (built-in with Python)
speech_recognition (for voice-to-text transcription, requires microphone access if used with real input)
Setup and Installation
Clone the Repository

bash
Copy code
git clone <repository-url>
cd voice-activated-upi-transaction
Install Required Libraries Install necessary Python packages:

bash
Copy code
pip install streamlit speechrecognition
Run the Application Start the application locally using Streamlit:

bash
Copy code
streamlit run app.py
Testing the Voice Command Feature

A simulated voice transcription is used in the absence of a real voice-to-text API.
Users can input text commands directly to test the transaction flow if microphone integration is not feasible.
Project Structure
app.py: Manages the Streamlit user interface, including login, transaction processing, and account management functions.
backend.py: Handles all backend operations, including database initialization, user validation, balance updates, and transaction processing.
transcriber.py: (optional) Can be used to manage audio recording and transcription if integrated with a voice-to-text service.
Code Explanation
backend.py
This file contains the database operations:

Database Initialization: Sets up a database with predefined users.
User Validation: Verifies login credentials for access control.
Transaction Processing: Deducts the specified amount from the sender’s balance and credits it to the recipient’s account if valid.
Balance Retrieval: Fetches and displays the user’s balance before and after each transaction.
app.py
This file includes the frontend elements:

Login System: Allows secure login for users with predefined credentials.
Transaction Interface: Users can record and transcribe voice commands to perform transactions.
Add/Delete User Functionality: Allows administrators to add or delete users directly from the UI.
Display Balance Changes: Shows “Balance Before Transaction” and “Balance After Transaction” separately after each transaction.
Example Workflow
Login: A user logs in using their username and password.
Balance Display: The user’s current balance is displayed upon login.
Start a Transaction:
Click on "Start Recording" to record a transaction command.
Click "Stop Recording and Transcribe" to generate text from the audio command.
Transaction Processing:
The transcription is parsed to detect the recipient and amount.
If the recipient exists in the database, the transaction proceeds, showing updated balances.
If the recipient doesn’t exist, the system prompts for re-recording.
Account Management:
Users can add a new account with a username, password, and initial balance.
Existing accounts can be deleted, which removes them from the database.
Logout: Users can log out to return to the main login page.
Known Limitations
User Base: Currently, limited to a predefined set of users. Extending to a larger user base would require a more scalable database.
Voice-to-Text Accuracy: Using a simulated transcription input, as real-time transcription accuracy depends on the API or library used.
Security: No encryption is implemented for passwords; however, this could be added for enhanced security in a real deployment.
Future Improvements
Real-Time Voice-to-Text Integration: Integrate a live voice recognition API for real-time transcription.
Enhanced Security: Implement encryption for credentials.
Scalability: Shift to a more robust database for handling a larger number of users.
Error Handling: Add more detailed error handling for unsupported voice commands.
Conclusion
The Voice-Activated UPI Transaction System is a practical demonstration of how voice commands can be used to enhance user experience in financial transactions. While it’s currently limited to a local environment, the project can be expanded and adapted for broader applications in the fintech domain, integrating features like real-time API calls and stronger security measures.
