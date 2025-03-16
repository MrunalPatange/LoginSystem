# Login System

## Description
This is a simple login system built using Python's Tkinter library. It provides a graphical user interface (GUI) for users to enter their username and password, which are then validated against predefined credentials.

## Features
- Background image for aesthetic design
- Login frame with username and password fields
- Error handling for empty fields and incorrect credentials
- A "Forgot Password" button (not yet functional)
- User authentication with a message box for success or failure

## Requirements
To run this application, you need to have Python installed along with the following dependencies:

```
pip install pillow
```

## Installation and Setup
1. Clone or download the project files.
2. Ensure you have the required dependencies installed.
3. Place a background image at the specified path: `D:/Python/PythonLoginSystem/Images/background.jpg`
4. Run the Python script:

```
python login.py
```

## Usage
1. Launch the application.
2. Enter the username and password.
3. Click the "Login" button.
4. If the credentials match, a success message appears.
5. If incorrect, an error message is displayed.

## Default Credentials
- **Username:** `Admin`
- **Password:** `Admin@1234`

## Issues
- The "Forgot Password" button is currently non-functional.
- The hardcoded username and password should be replaced with a more secure authentication system.
- Incorrect username validation logic: `!= " Mrunal "` should be `!= "Mrunal"` (extra spaces need to be removed).

## Contribution
Feel free to contribute to the project by enhancing the login mechanism or adding database support.

## License
This project is free to use and modify.

---
### Author
Developed by **Mrunal**

