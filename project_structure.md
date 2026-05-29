# Project Folder Structure

```
ProgrammingPracticesPlatform/
│
├── assets/                     # Images, icons, fonts, UI assets
├── database/                  # SQLite DB and schema definitions
│   └── schema.sql
├── docs/                      # Documentation (installation, user guide, developer guide)
│   ├── README.md
│   ├── INSTALL.md
│   ├── USER_MANUAL.md
│   └── DEV_GUIDE.md
├── logs/                      # Application logs (runtime logs, error logs)
├── modules/                   # Core application modules (each a package)
│   ├── __init__.py
│   ├── auth/                  # Authentication & user management
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── validators.py
│   ├── dashboard/             # Main dashboard UI components
│   │   ├── __init__.py
│   │   └── dashboard.py
│   ├── quizzes/               # Quiz engine and related models
│   │   ├── __init__.py
│   │   ├── quiz.py
│   │   ├── question.py
│   │   └── result.py
│   ├── challenges/            # Coding challenges module
│   │   ├── __init__.py
│   │   └── challenge.py
│   ├── leaderboard/           # Leaderboard & ranking
│   │   ├── __init__.py
│   │   └── leaderboard.py
│   ├── profile/               # User profile and stats
│   │   ├── __init__.py
│   │   └── profile.py
│   ├── settings/              # Application settings UI and persistence
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── admin/                 # Administration tools and UI
│   │   ├── __init__.py
│   │   └── admin.py
│   └── database/              # Database abstraction layer
│       ├── __init__.py
│       └── db.py
├── tests/                     # Unit and integration tests
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_db.py
│   └── test_quiz.py
├── utils/                     # Helper utilities (logging, configuration)
│   ├── __init__.py
│   ├── logger.py
│   └── config.py
├── main.py                    # Application entry point
├── requirements.txt            # Python dependencies
├── README.md                  # Project overview for GitHub
└── .gitignore                 # Ignored files and directories
```

The directories will be created automatically when the first file inside each is written.
