import os
from datetime import datetime, timedelta
import calendar

START_DATE = datetime(2025, 1, 1)

def get_day_count(start_date, today):
    """Calculate the total days since the start date."""
    return (today - start_date).days + 1  # Include today

def check_file_validity(file_path):
    """Check if the file contains a Python class and the word 'approach'."""
    if not os.path.exists(file_path):
        return False

    with open(file_path, "r") as file:
        content = file.read()
        return "class " in content and "approach" in content

def check_day_folder(day_folder):
    """Check the status of a day's folder."""
    files = ["1.py", "2.py"]
    file_status = [check_file_validity(os.path.join(day_folder, file)) for file in files]

    if all(file_status):
        return "✅"  # Both files exist and meet criteria
    elif any(file_status):
        return "🟡"  # Only one file exists and meets criteria
    else:
        return "❌"  # Neither file exists or meets criteria

def format_monthly_streak(start_date, total_days):
    """Format streak status for each month."""
    today = datetime.now().date()
    streak = {}
    day_number = 1
    current_date = start_date.date()

    while day_number <= total_days:
        year, month = current_date.year, current_date.month
        first_weekday, days_in_month = calendar.monthrange(year, month)

        # Initialize month entry if not exists
        if month not in streak:
            streak[month] = {
                "name": current_date.strftime("%B %Y"),
                "days": [" "] * first_weekday,  # Leading empty spaces for alignment
                "completed": True  # Assume completed until proven otherwise
            }

        # Add day's status
        day_folder = os.path.join("Solution", f"Day {day_number}")
        if day_number <= total_days and current_date <= today:
            status = check_day_folder(day_folder)
            streak[month]["days"].append(status)
            if status != "✅":
                streak[month]["completed"] = False  # Mark incomplete
        else:
            streak[month]["days"].append(" ")

        # Move to the next day
        current_date += timedelta(days=1)
        day_number += 1

    return streak

def update_readme(streak_data):
    """Update README with streak data."""
    readme_file = "README.md"
    content = []

    content.append("# Leetcode Challenge\n")
    content.append("## Daily Streak\n\n")

    for month, data in streak_data.items():
        days = " ".join(data["days"])
        badge = " 🏆" if data["completed"] else ""
        content.append(f"### {data['name']}{badge}\n")
        content.append(f"{days}\n\n")

    today = datetime.now().strftime("%B %d, %Y")
    content.append(f"Last Updated: {today}\n")

    with open(readme_file, "w") as file:
        file.writelines(content)

    print("README.md updated successfully.")

def main():
    today = datetime.now()
    total_days = get_day_count(START_DATE, today)
    streak_data = format_monthly_streak(START_DATE, total_days)
    update_readme(streak_data)

if __name__ == "__main__":
    main()
