```mermaid
classDiagram
class WeatherDashboardApp {
  +start()
  +show_main_view()
  -current_user: User
  -db: DatabaseManager
}
class MainView {
  +render()
  +on_refresh()
}
class SettingsView
class WeatherController {
  +fetch_weather(location)
  +apply_preferences()
}
class DatabaseManager {
  +connect()
  +save_pref(user, prefs)
  +get_pref(user)
}
class APIClient {
  +get_weather(location)
}

WeatherDashboardApp --> MainView
WeatherDashboardApp --> SettingsView
WeatherDashboardApp --> WeatherController
WeatherController --> APIClient
WeatherController --> DatabaseManager
DatabaseManager <|-- DatabaseManager
APIClient --> "External Weather API"
```