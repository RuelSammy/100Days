import schedule
import time
import datetime

# Define the tasks
def send_introduction_email():
    print(f"{datetime.datetime.now()}: Sending email introducing myself.")

def walk_alarm():
    print(f"{datetime.datetime.now()}: Alarm! Time to take a walk.")

def lunch_reminder():
    print(f"{datetime.datetime.now()}: Reminder: Time for lunch!")

def check_in_task():
    print(f"{datetime.datetime.now()}: Checking in on progress for the day.")

def tea_break_reminder():
    print(f"{datetime.datetime.now()}: Tea break time! Relax a bit.")

def wrap_up_summary():
    print(f"{datetime.datetime.now()}: Start wrapping up today's activities. Summarize tasks completed.")

# Schedule the tasks
schedule.every().day.at("08:00").do(send_introduction_email)
schedule.every().day.at("10:00").do(walk_alarm)
schedule.every().day.at("12:30").do(lunch_reminder)
schedule.every().day.at("15:00").do(check_in_task)
schedule.every().day.at("16:00").do(tea_break_reminder)
schedule.every().day.at("18:00").do(wrap_up_summary)

# Keep running
while True:
    schedule.run_pending()
    time.sleep(30)  # Check every 30 seconds
