import random
import datetime
import pytz
import os
import time

# Decide whether or not to push on this day (75% push rate)
should_push_today = random.randrange(1, 13) > 3

log_est_now = pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone("America/Toronto"))
log_formatted_est_now = log_est_now.strftime("%A, %B %d, %Y - %I:%M:%S %p")
push_status = "[PUSH]" if should_push_today else "[NO PUSH]"
with open("log.txt", "a") as log:
    log.write(f"\n{push_status} {log_formatted_est_now}")
log.close()

if should_push_today:
    num_of_contributions = random.randrange(1, 11)
    for x in range(num_of_contributions):
        # Generate formatted date and time in EST
        with open("datetimes.txt", "a") as datetimes:
            utc_now = pytz.utc.localize(datetime.datetime.utcnow())
            est_timezone = pytz.timezone("America/Toronto")
            est_now = utc_now.astimezone(est_timezone)
            formatted_est_now = est_now.strftime("%A, %B %d, %Y - %I:%M:%S %p")
            datetimes.write(f"\n{formatted_est_now}")
            os.system(f"git add . && git commit -m {round(time.time())}")
        datetimes.close()
    os.system("git push origin main")
