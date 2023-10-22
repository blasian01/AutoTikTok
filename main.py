import os
import time
import schedule

def run_scripts():
    # List of Python scripts to run
    python_scripts = [
        "mainCar.py",
        "mainAnime.py",
        "mainReddit.py"
    ]

    # Run each script one by one
    for script in python_scripts:
        print(f"Running {script}...")
        os.system(f"python {script}")
        print(f"{script} completed.")

# Schedule to run every day at 12 PM
schedule.every().day.at("12:00").do(run_scripts)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
