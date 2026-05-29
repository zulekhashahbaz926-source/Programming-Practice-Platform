# USER_MANUAL.md

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ProgrammingPracticesPlatform.git
cd ProgrammingPracticesPlatform

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # on Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## First Run

```bash
python src/main.py  # or `python -m src.app`
```

The application will launch with a login screen.

## Register a New Account
1. Click **Register** on the login screen.
2. Fill in **Username**, **Password**, and optional **Email**.
3. Password must meet the complexity rules (uppercase, lowercase, digit, special character, min 8 chars).
4. Press **Submit** – you will be redirected to the login page.

## Login
1. Enter your credentials and press **Login**.
2. Upon success you will see the **Dashboard**.

## Dashboard Overview
- **Progress cards** show completed exercises, total score and accuracy.
- **Sidebar navigation** lets you switch to **Exercises**, **Challenges**, or **Settings**.

## Working with Exercises
1. Choose an exercise from the list (filter by difficulty if desired).
2. The **Exercise View** shows the problem description and a code editor.
3. Write your solution and click **Submit**.
4. Immediate feedback appears – correct/incorrect with a hint.
5. Successful completion updates your progress automatically.

## Challenges
1. Navigate to **Challenges** via the sidebar.
2. Select a difficulty (Easy, Medium, Hard).
3. A random challenge is generated; complete it within the allotted time (timer shown).
4. After submission you receive feedback and the result is stored.

## Settings
- Toggle **Dark/Light** mode.
- Update your profile information (display name, email).
- Adjust preferences such as default difficulty.

## Data Persistence
All user data, progress and challenges are stored in a SQLite database located in the user’s home directory (`%USERPROFILE%/ProgrammingPracticesPlatform/data`).

## Troubleshooting
- **Forgot password** – currently not implemented; contact the developer.
- **Database errors** – delete the database file to start fresh (data will be lost).
- **UI does not appear** – ensure CustomTkinter is installed and your Python version is >=3.9.

---
*End of User Manual*
