# AI Wrapped
AI wrapped provides an AI-generated summary of your 2023 year given data from various platforms (Facebook, Google Calendar, Whoop, etc...). I built AI wrapped to help me look back on what I did during my year. I always struggle with logging all the things I want to log about my day and figured that a lot of the information already exists online. For me, that's in my photos, my workout logs, and my messages with friends and family. I built a little tool to generate a summary of my year, day-by-day for the year of 2023. It turned out pretty good!

# How To Use It
To use the tool, you first need to download your data. A lot of companies offer the opportunity to export your data into files which is what this tool uses to generate the summary. Right now, the tool supports the following data:

- Facebook (Messenger)
- Google Calendar
- Whoop

All of the data needs to be downloaded into the `data` directory at the root of this project. The data sources aren't required for the tool to work. Here is where all the data for each of the data sources should go and how you can acquire the data:

## Facebook (Messenger)
Follow the these instructions to download your data from Facebook: https://www.facebook.com/help/212802592074644. Right now, the tool only supports data from Facebook Messenger, so it's not necessary to download non Facebook Messenger data.

Once Facebook has made your data available, you need to move the data into the `data` folder in this repository in a folder called `your_activity_across_facebook`. Note that if you have a lot of data in Facebook, Facebook will export them in separate 10GB zip files. After downloading them, you may need to consolidate it into one zip file. You can do this by recursively copying the contents of each unzipped folders to one "main" folder.

## Google Calendar
Follow these directions to download your Google Calendar data as an ics file: https://support.google.com/calendar/answer/37118?hl=en&co=GENIE.Platform%3DDesktop. This tool converts requires a csv file with a specific format instead of an ics file. To convert the ics file to a csv file with the expected format, convert the ics file using this online tool: https://www.indigoblue.eu/ics2csv/.

Place the resulting csv file in the `data` directory inside a `calendar` folder.

## Whoop
Follow these instructions to download your Whoop data: https://support.whoop.com/s/article/How-to-Export-Your-Data. After unzipping the folder that Whoop provides, place the csv files inside the `data` directory inside a `whoop` folder.

## Integrations Coming Soon

- Google Photos
- Strava

## Generating a 2023 Summary
To generate a 2023 summary after adding the relevant data to `data`, follow these instructions:

1. Create a virtual Python environment with `python3 -m venv venv`
2. Run `source venv/bin/activate` to activate the virtual environment
3. Install the Python dependencies with `pip install -r requirements.txt`
4. Run `python index.py`