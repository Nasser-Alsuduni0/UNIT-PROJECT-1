# FitTrack - Personal Fitness Tracking Application

## Overview

FitTrack is a comprehensive command-line fitness tracking application built in Python that helps users monitor their workouts, track calorie intake, set fitness goals, and track their progress over time. The application features a user-friendly interface with rich text formatting and provides detailed analytics to help users stay motivated and achieve their fitness objectives.

## Features

- **User Profile Management**: Create and manage personal profiles with weight, height, and BMI calculations
- **Workout Tracking**: Log different types of workouts with duration, distance, and sets
- **Calorie Tracking**: Record daily meals and monitor calorie intake
- **Goal Setting**: Set personalized fitness goals including target weight, weekly workout targets, and daily calorie limits
- **Progress Analytics**: View detailed progress reports and analytics
- **Data Persistence**: All data is saved locally in JSON format for easy access and backup

## User Stories

### As a fitness enthusiast, I want to:
- **Track my workouts** so that I can monitor my exercise routine and progress
- **Log my meals and calories** so that I can maintain a healthy diet
- **Set personal fitness goals** so that I have clear targets to work towards
- **View my progress over time** so that I can stay motivated and adjust my routine
- **Calculate my BMI** so that I can understand my current health status
- **Monitor my weight changes** so that I can track my fitness journey

### As a beginner, I want to:
- **Create a simple profile** so that I can get started quickly
- **Set achievable goals** so that I don't get overwhelmed
- **Get clear feedback** on my progress so that I can stay motivated
- **Have my data saved automatically** so that I don't lose my progress

### As an advanced user, I want to:
- **View detailed analytics** so that I can optimize my fitness routine
- **Track multiple workout types** so that I can maintain a varied exercise program
- **Monitor weekly and daily progress** so that I can make data-driven decisions
- **Export my data** so that I can analyze it in other tools

## Usage

### Prerequisites

- Python 3.7 or higher
- Required packages (install via pip):
  ```bash
  pip install rich
  ```

### Installation

1. Clone or download the project files
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   (If requirements.txt doesn't exist, install rich manually)

### Running the Application

1. Start the application:
   ```bash
   python main.py
   ```

2. **First Time Setup**:
   - Enter your name, weight (kg), and height (cm)
   - The app will calculate your BMI and provide health recommendations
   - Set your fitness goals (target weight, weekly workouts, daily calorie limit)

3. **Main Menu Options**:
   - **Workout Tracker**: Add, view, and analyze your workouts
   - **Calorie Tracker**: Log meals and track daily calorie intake
   - **Goals & Progress**: View progress towards your fitness goals
   - **Quit**: Exit the application

### Workout Tracking

- Add workouts with details like:
  - Workout type (running, weightlifting, etc.)
  - Duration in minutes
  - Distance (for running)
  - Number of sets (for strength training)
- View all recorded workouts in a formatted table
- Access workout analytics and summaries

### Calorie Tracking

- Log meals with:
  - Meal name
  - Calorie content
  - Date
- View daily calorie intake
- Access calorie analytics and trends

### Progress Monitoring

- Track progress towards:
  - Weight goals
  - Weekly workout targets
  - Daily calorie limits
- View current status vs. targets
- Update goals as needed

## Data Storage

All data is stored locally in the `data/` directory:
- `workouts.json`: Workout entries
- `calories.json`: Calorie/meal entries
- `goals.json`: User fitness goals

## Project Structure

```
FitTrack/
├── main.py              # Main application entry point
├── profile.py           # User profile management
├── goals.py             # Goal setting and progress tracking
├── workout_tracker/     # Workout tracking module
│   ├── workout.py       # Workout data model
│   ├── user_input.py    # Workout input handling
│   ├── storage.py       # Workout data persistence
│   └── analytics.py     # Workout analytics
├── calorie_tracker/     # Calorie tracking module
│   ├── calorie.py       # Calorie data model
│   ├── user_input.py    # Calorie input handling
│   ├── storage.py       # Calorie data persistence
│   └── analytics.py     # Calorie analytics
└── data/                # Data storage directory
```

## Contributing

This is a personal fitness tracking application. Feel free to fork and modify for your own use or contribute improvements.

## License

This project is open source and available under the MIT License.





