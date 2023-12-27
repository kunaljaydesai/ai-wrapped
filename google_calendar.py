from zoneinfo import ZoneInfo
import csv
from datetime import datetime

# use this to convert ics to csv file
# https://www.indigoblue.eu/ics2csv/

events_csv = 'data/calendar/kunaljaydesai.csv'

def get_calendar_events():
    with open(events_csv, 'r') as csvfile:
        events_reader = csv.reader(csvfile, delimiter=',')
        headers = next(events_reader)
        return list(filter(lambda e: bool (e), [dict(zip(headers, i)) for i in events_reader]))

DATE_TIME_FORMAT = '%m/%d/%Y %I:%M %p'
TIME_ZONE = ZoneInfo('America/Los_Angeles')

def get_calendar_activities():
    raw_events = get_calendar_events()
    activities = []
    for event in raw_events:
        activities.append({
           'start' : datetime.strptime(event['DTSTART'], DATE_TIME_FORMAT).replace(tzinfo=TIME_ZONE),
           'end' : datetime.strptime(event['DTEND'], DATE_TIME_FORMAT).replace(tzinfo=TIME_ZONE),
           'description': event['SUMMARY'],
           'type': 'Calendar Event',
        })
    return activities
