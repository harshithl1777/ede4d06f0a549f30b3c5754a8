import random
import datetime
import pytz
import subprocess
import time

# Decide whether or not to push on this day (75% push rate)
should_push_today = random.randrange(1, 13) > 3

if should_push_today:
    num_of_contributions = random.randrange(1, 11)

    with open("datetimes.txt", "a") as datetimes:
        for x in range(num_of_contributions):
            # Generate formatted date and time in EST
            utc_now = pytz.utc.localize(datetime.datetime.utcnow())
            est_timezone = pytz.timezone("America/Toronto")
            est_now = utc_now.astimezone(est_timezone)
            formatted_est_now = est_now.strftime("%A, %B %d, %Y - %I:%M:%S %p")
            datetimes.write(f"\n{formatted_est_now}")
        datetimes.close()
    subprocess.run(
        [
            "git",
            "add",
            ".",
            "&&",
            "git",
            "commit",
            "-m",
            f"{round(time.time())}",
            "&&",
            "git",
            "push",
            "origin",
            "master",
        ]
    )
