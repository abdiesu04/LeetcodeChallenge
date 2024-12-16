import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import random

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "abdiesayas33@gmail.com"       # Your email address
PASSWORD = "tlnj jiuo qhpx msmu"       # Your email app password
RECIPIENTS = [("Abdi", "abdiesayasbayisa@gmail.com"), ("Tamirat", "tamiratkebede120@gmail.com")]  # Recipient names and emails

# Load Excel sheet
EXCEL_FILE = "leetcode_problems.xlsx"
data = pd.read_excel(EXCEL_FILE)

# Start date
START_DATE = datetime(2024, 12, 16)  # Your starting date

# Quotes for each day of the week
quotes = {
    "Monday": [
        "The journey of a thousand miles begins with a single step.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "Focus on progress, not perfection.",
        # Add 27 more motivational quotes for Monday
    ],
    "Tuesday": [
        "Dream big and dare to fail.",
        "What seems impossible today will one day become your warm-up.",
        "Believe in yourself and all that you are.",
        # Add 27 more motivational quotes for Tuesday
    ],
    "Wednesday": [
        "Your only limit is your mind.",
        "Be stronger than your excuses.",
        "Don’t watch the clock; do what it does. Keep going.",
        # Add 27 more motivational quotes for Wednesday
    ],
    "Thursday": [
        "Push yourself, because no one else is going to do it for you.",
        "The hard days are what make you stronger.",
        "Consistency is what transforms average into excellence.",
        # Add 27 more motivational quotes for Thursday
    ],
    "Friday": [
        "Wake up with determination, go to bed with satisfaction.",
        "The future depends on what you do today.",
        "You don’t have to be great to start, but you have to start to be great.",
        # Add 27 more motivational quotes for Friday
    ],
    "Saturday": [
        "Believe you can, and you’re halfway there.",
        "Act as if what you do makes a difference. It does.",
        "Hardships often prepare ordinary people for an extraordinary destiny.",
        # Add 27 more motivational quotes for Saturday
    ],
    "Sunday": [
        "Perseverance is not a long race; it is many short races one after another.",
        "Do something today that your future self will thank you for.",
        "Small steps every day lead to big results.",
        # Add 27 more motivational quotes for Sunday
    ],
}

# Function to calculate the day number
def get_day_number():
    today = datetime.now()
    delta = today - START_DATE
    return delta.days + 1  # Add 1 because Day 1 starts on Dec 16, 2024

# Function to get today's motivational quote
def get_motivational_quote():
    today = datetime.now()
    weekday = today.strftime("%A")  # Get the current weekday (e.g., Monday, Tuesday)
    return random.choice(quotes[weekday])  # Randomly pick a quote for the current weekday

# Function to send personalized email
def send_email(name, email, day_number, problem1_title, problem1_link, problem2_title, problem2_link, quote):
    try:
        # Create email
        subject = f"📧 LeetCode Challenges - Day {day_number}"
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <h1 style="color: #4CAF50;">Hello {name},</h1>
            <p>Today is <strong>Day {day_number}</strong> of your LeetCode challenge!</p>
            <p>Here are your problems for the day:</p>
            <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
                <thead>
                    <tr style="background-color: #f2f2f2;">
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Problem</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Link</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">{problem1_title}</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">
                            <a href="{problem1_link}" style="color: #1E90FF;">{problem1_link}</a>
                        </td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">{problem2_title}</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">
                            <a href="{problem2_link}" style="color: #1E90FF;">{problem2_link}</a>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p><strong>Motivational Quote for Today:</strong></p>
            <blockquote style="font-size: 1.2em; color: #555; border-left: 4px solid #4CAF50; padding-left: 10px; margin: 20px 0;">
                "{quote}"
            </blockquote>
            <p>Happy coding! 🚀</p>
            <footer style="margin-top: 30px; text-align: center; font-size: 12px; color: #aaa;">
                <p>Automated by Python | LeetCode Daily Challenges</p>
            </footer>
        </body>
        </html>
        """

        # Create email object
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, email, msg.as_string())

        print(f"✅ Email for {name} (Day {day_number}) sent successfully!")

    except Exception as e:
        print(f"❌ Failed to send email for {name} (Day {day_number}): {e}")

# Select problems for the current day
def get_daily_problems(data, day_number):
    # Use modulo to loop back if the day number exceeds the total rows
    problem1_row = data.iloc[(2 * (day_number - 1)) % len(data)]
    problem2_row = data.iloc[(2 * (day_number - 1) + 1) % len(data)]
    return problem1_row['Problem Title'], problem1_row['Link'], problem2_row['Problem Title'], problem2_row['Link']

# Main execution
if __name__ == "__main__":
    day_number = get_day_number()
    problem1_title, problem1_link, problem2_title, problem2_link = get_daily_problems(data, day_number)
    quote = get_motivational_quote()

    for name, email in RECIPIENTS:
        send_email(name, email, day_number, problem1_title, problem1_link, problem2_title, problem2_link, quote)
