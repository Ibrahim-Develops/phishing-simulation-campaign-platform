import datetime
import os

LOG_FOLDER = "logs"
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

def log_event(event_type, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] [{event_type}] {message}\n"

    with open(f"{LOG_FOLDER}/campaign.log", "a") as f:
        f.write(log_message)
