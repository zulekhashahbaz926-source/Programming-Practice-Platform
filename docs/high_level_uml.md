# High-Level UML Diagrams for Zyntriva

This file contains four standard UML diagrams (Use Case, Class, Activity, Sequence) in Mermaid syntax. Paste into any Mermaid renderer or Markdown preview that supports Mermaid.

Generated PNG versions are available in:

- `docs/uml_use_case.png`
- `docs/uml_class_diagram.png`
- `docs/uml_activity_diagram.png`
- `docs/uml_sequence_diagram.png`


## 1) Use Case Diagram
```mermaid
usecaseDiagram
actor User
actor Admin
User --> (Register / Login)
User --> (View Dashboard)
User --> (Attempt Problem)
User --> (Run Tests)
User --> (Participate in Peer Review)
User --> (View Reports)
Admin --> (Manage Problems)
Admin --> (Seed Data)
Admin --> (Deploy Application)
(Manage Problems) ..> (View Dashboard) : <<include>>
(Seed Data) ..> (Manage Problems) : <<extend>>
```

## 2) Class Diagram
```mermaid
classDiagram
class ZyntrivaApp {
  +main()
  +show_frame(name)
  -current_user
  -db : DatabaseManager
}
class AuthView {
  +build_interface()
  +login_user()
  +register_user()
}
class AuthController {
  +register_user(...)
  +authenticate_user(...)
}
class DashboardView {
  +build_layout()
  +render_module(name)
  +update_stats()
}
class DashboardController {
  +load_module_data(name)
  +get_dashboard_stats()
}
class DatabaseManager {
  +initialize_schema()
  +create_user(...)
  +execute(query, params)
  +get_commits()
}
class Module {
  +get_overview()
}
class ProcessModelModule
class VersionControlModule

ZyntrivaApp --> AuthView : hosts
ZyntrivaApp --> DashboardView : hosts
ZyntrivaApp *-- DatabaseManager : owns
AuthView --> AuthController : uses
AuthController --> DatabaseManager : queries/writes
DashboardView --> DashboardController : uses
DashboardController --> Module : loads
Module <|-- ProcessModelModule
Module <|-- VersionControlModule
AuthController ..> Exceptions : throws
AuthController ..> Validators : uses
```

## 3) Activity Diagram (Login flow)
```mermaid
flowchart TD
    Start([Start]) --> EnterCreds[Enter username/email and password]
    EnterCreds --> Validate{Validate input}
    Validate -->|invalid| ShowError[Show validation error]
    ShowError --> Retry{Try again?}
    Retry -->|yes| EnterCreds
    Retry -->|no| End([End])
    Validate -->|valid| Authenticate[Authenticate with AuthController]
    Authenticate --> DBQuery[Query DatabaseManager for user]
    DBQuery --> AuthResult{User found and password match?}
    AuthResult -->|no| ShowAuthFail[Show authentication failure]
    ShowAuthFail --> Retry
    AuthResult -->|yes| ShowDashboard[Load DashboardView]
    ShowDashboard --> End
```

## 4) Sequence Diagram (Login)
```mermaid
sequenceDiagram
    participant User
    participant AuthView
    participant AuthController
    participant DatabaseManager
    participant DashboardView

    User->>AuthView: submit credentials
    AuthView->>AuthController: authenticate(username, password)
    AuthController->>DatabaseManager: find_user_by_username(username)
    DatabaseManager-->>AuthController: user_row / null
    alt user found
        AuthController->>DatabaseManager: verify_password(hash)
        DatabaseManager-->>AuthController: verification_result
        alt password valid
            AuthController-->>AuthView: authentication_success(user_info)
            AuthView->>DashboardView: show_frame("Dashboard")
            DashboardView-->>AuthView: rendered
            AuthView-->>User: display dashboard
        else password invalid
            AuthController-->>AuthView: authentication_failed("Invalid password")
            AuthView-->>User: display error
        end
    else user not found
        AuthController-->>AuthView: authentication_failed("User not found")
        AuthView-->>User: display error
    end
```
