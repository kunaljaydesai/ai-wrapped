import os
import csv
from datetime import datetime

from settings import TIME_ZONE

dir_path = os.path.dirname(os.path.realpath(__file__))
def get_sleeps():
    with open(f'{dir_path}/data/whoop/sleeps.csv', newline='') as csvfile:
        sleep_reader = csv.reader(csvfile, delimiter=',')
        headers = next(sleep_reader)
        return [dict(zip(headers, i)) for i in sleep_reader]

def get_workouts():
    with open(f'{dir_path}/data/whoop/workouts.csv', newline='') as csvfile:
        workout_reader = csv.reader(csvfile, delimiter=',')
        headers = next(workout_reader)
        return [dict(zip(headers, i)) for i in workout_reader]
    
DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def get_sleep_activities():
    raw_sleeps = get_sleeps()
    sleep_activity = []
    for sleep in raw_sleeps:
        cycle_start = sleep['Sleep onset']
        cycle_end = sleep['Wake onset']
        if cycle_start and cycle_end:
            sleep_activity.append({
                'start' : datetime.strptime(cycle_start, DATE_TIME_FORMAT).replace(tzinfo=TIME_ZONE),
                'end': datetime.strptime(cycle_end, DATE_TIME_FORMAT).replace(tzinfo=TIME_ZONE),
                'description': 'Sleep',
                'type': 'Sleep',
            })
    return sleep_activity

def get_workout_activities():
    raw_workouts = get_workouts()
    workout_activity = []
    for workout in raw_workouts:
        start = workout['Workout start time']
        end = workout['Workout end time']
        if start and end:
            workout_activity.append({
                'start' : datetime.strptime(start, DATE_TIME_FORMAT).replace(tzinfo=TIME_ZONE),
                'end': datetime.strptime(end, DATE_TIME_FORMAT).replace(tzinfo=TIME_ZONE),
                'description': f"{workout['Activity name']} with a {workout['Activity Strain']} strain score out of 20",
                'type': 'workout',
            })
    return workout_activity
            