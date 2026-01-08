import random
import datetime
import pytz
import os
import time

tz = pytz.timezone("America/Toronto")

# Decide whether or not to push on this day (75% push rate)
should_push_today = random.randrange(1, 13) > 3

# Correct timezone handling
log_est_now = datetime.datetime.now(pytz.UTC).astimezone(tz)
log_formatted_est_now = log_est_now.strftime("%A, %B %d, %Y - %I:%M:%S %p")

push_status = "[PUSH]" if should_push_today else "[NO PUSH]"
with open("log.txt", "a") as log:
    log.write(f"\n{push_status} {log_formatted_est_now}")

if should_push_today:
    num_of_contributions = random.randrange(1, 11)

    for _ in range(num_of_contributions):
        est_now = datetime.datetime.now(pytz.UTC).astimezone(tz)
        formatted_est_now = est_now.strftime("%A, %B %d, %Y - %I:%M:%S %p")

        with open("datetimes.txt", "a") as datetimes:
            datetimes.write(f"\n{formatted_est_now}")

        os.system(f'git add . && git commit -m "{int(time.time())}"')

    os.system("git push origin main")
