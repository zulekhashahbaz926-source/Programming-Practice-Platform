```mermaid
flowchart TB
  subgraph UI [Tkinter Weather Dashboard]
    UI_App[WeatherDashboardApp]
    UI_Views[Views (Main, Settings, Forecast)]
  end

  subgraph Client
    User[User]
  end

  subgraph Backend
    AppModule[App Controller]
    Cache[Cache]
    DB[(SQLite DB)]
    Scheduler[Scheduler]
  end

  subgraph Services
    WeatherAPI[/Weather API Service/]
    NotificationSvc[/Notification Service/]
    AnalyticsSvc[/Analytics Service/]
    PrefsSvc[/User Preferences Service/]
  end

  User -->|interacts| UI_App
  UI_App --> UI_Views
  UI_App --> AppModule
  AppModule --> WeatherAPI
  AppModule --> PrefsSvc
  AppModule --> NotificationSvc
  AppModule --> AnalyticsSvc
  AppModule --> DB
  AppModule --> Cache
  WeatherAPI -->|HTTP| Services["External Weather Providers"]

  classDef svc fill:#f9f9f9,stroke:#333,stroke-width:1px
  class WeatherAPI,NotificationSvc,AnalyticsSvc,PrefsSvc svc
```