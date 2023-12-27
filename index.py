from datetime import datetime, timedelta
import dbm
import pickle

from google_calendar import get_calendar_activities
from whoop import get_sleep_activities, get_workout_activities
from facebook import get_messages
from settings import YEAR, TIME_ZONE


activities = sorted(
    get_messages() +
    get_calendar_activities() + 
    get_sleep_activities() + 
    get_workout_activities(), 
    key=lambda x: x['start'] 
)    
activities_this_year = sorted(list(filter(lambda x: x['start'].year == YEAR, activities)), key=lambda x: x['start'])

activity_idx = 0
current_date = datetime(year=YEAR, month=1, day=1, tzinfo=TIME_ZONE)

pickle.dump(activities_this_year, open("activities_this_year.pickle", "wb"))

activities_per_day = {} 
activities_per_day[current_date] = []
FILE_NAME = "2023.md-test2"
with open(FILE_NAME, "w") as f:
    f.write(f"## {current_date.strftime('%b %d, %Y')}")
    f.write("\n\n")
    while activity_idx < len(activities_this_year):
        activity = activities_this_year[activity_idx]
        if activity['start'].astimezone(TIME_ZONE).date() > current_date.date():
            current_date = current_date + timedelta(days=1)
            f.write(f"## {current_date.strftime('%b %d, %Y')}")
            f.write("\n\n")
            activities_per_day[current_date] = []
        else:
            f.write(f"{activity['type']} ({activity['start'].astimezone(TIME_ZONE).strftime('%m/%d/%Y %I:%M %p')} - {activity['end'].astimezone(TIME_ZONE).strftime('%m/%d/%Y %I:%M %p')}): {activity['description']}")
            f.write("\n\n")
            activity_idx += 1
            activities_per_day[current_date].append(activity)


from openai import OpenAI 
client = OpenAI()

SUMMARY_FILE_NAME = "2023-summary-2.md"
with open(SUMMARY_FILE_NAME, "w") as f:
    for day, activities in sorted(activities_per_day.items(), key=lambda x: x[0]):
        f.write(f"## {day.strftime('%b %d, %Y')}")
        f.write("\n\n")
        description = ""
        for activity in activities:
            description += (f"{activity['type']} ({activity['start'].astimezone(TIME_ZONE).strftime('%m/%d/%Y %I:%M %p')} - {activity['end'].astimezone(TIME_ZONE).strftime('%m/%d/%Y %I:%M %p')}): {activity['description']}")
            description += "\n\n"
        with dbm.open('summary-day', 'c') as db:
            db[description] = client.chat.completions.create(
                model="gpt-3.5-turbo-16k",
                max_tokens=45,
                messages=[
                    {"role": "system", "content": "You are an AI used to find the highlights in Kunal's day based on context clues from workout activity, Facebook messages, and Google Calendar events."},
                    {"role": "user", "content": f"Find and summarize the highlights of this day in less than 30 words {day.astimezone(TIME_ZONE).strftime('%m/%d/%Y %I:%M %p')}:\n\n{description}"},
                ]
            ).choices[0].message.content
            f.write(str(db[description]))
            f.write("\n\n")
