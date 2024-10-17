import os
import requests
import pandas as pd
from datetime import datetime

# Step 1: Correct Google Sheets download URL format
huistakenURL = "https://docs.google.com/spreadsheets/d/1KvUvxK7MPfCXKifQ_biml9cmto6CcQ8UPR5lm4kVwjc/export?format=xlsx"
afwasRoosterURL = "https://docs.google.com/spreadsheets/d/1YO39jobgWjv6uNDabw3qdShkKv3RSR1W04Ux3q1h3yg/export?format=xlsx"

# Step 2: Define the local file path
huistaakRoosterPath = "huistaakRooster.xlsx"
afwasRoosterPath = "afwasrooster.xlsx"

errorLog = []

# Step 3: Check if the file already exists
def getExcelFiles(url, path, forceDownload = False):
    if not os.path.exists(path) or forceDownload:
        # Step 4: Download the Excel file
        print(f"downlaoding url:{url}")
        response = requests.get(url)
        
        # Step 5: Save the file locally
        with open(path, "wb") as file:
            file.write(response.content)
        
        print(f'Downloaded: {path}')
    else:
        print(f'File already exists: {path}')

def capitalizeFirstLetter(s):
    if len(s) > 0 and not s[0].isupper():
        return s[0].upper() + s[1:]
    return s


def getTodaysDishWasher():
    # Read the Excel file
    df = pd.read_excel(afwasRoosterPath, engine='openpyxl')
    
    # Get today's date in the format matching the 'DAG' column
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Filter the dataframe for today's date
    today_row = df[df['DAG'] == today]
    
    if not today_row.empty:
        # Get the name of the person
        person = today_row['PERSOON'].values[0]
        print(f"Today's dishwasher: {person}")
        return capitalizeFirstLetter(person)
    else:
        print("No entry found for today's date.")
    
    return None

def getTaskFromContactName(name):
    # Load the Excel file into a DataFrame without a header
    df = pd.read_excel(huistaakRoosterPath, engine='openpyxl', header=None)
    
    # Get today's date in the format that matches the DataFrame's date entries
    today = datetime.now().strftime('%Y-%m-%d 00:00:00')
    # today = '2024-09-02 00:00:00'
    # Extract the date row (the second row) to get the actual date values
    date_row = df.iloc[1].apply(lambda x: x.split(' ')[0] + ' 00:00:00' if isinstance(x, str) else x)  # Clean dates
    
    # Check if the name is in the first column of the DataFrame
    if name in df.iloc[:, 0].values:
        # Locate the row index for the given name
        row_index = df.index[df.iloc[:, 0] == name].tolist()[0]
        
        # Get the index of today's date in the cleaned date row
        today_index = date_row[date_row == today].index
        
        if not today_index.empty:  # If today's date is found in the date row
            task_index = today_index[0]  # Get the first index
            task = df.at[row_index, task_index]
            if pd.notna(task):  # Check if the task is not NaN
                return task
            else:
                errorLog.append(f"{name} has no task assigned for today.")
                return None
        else:
            errorLog.append("Today's date not found in the schedule.")
            return None
    else:
        errorLog.append(f"{name} is not found in the schedule.")
        return None



def init():
    getExcelFiles(huistakenURL, huistaakRoosterPath, True)
    getExcelFiles(afwasRoosterURL, afwasRoosterPath, True)



# Step 6: Read the Excel file into a Pandas DataFrame
# df = pd.read_excel(huistaakRoosterPath, engine='openpyxl')

# date_column_name = f"2024-09-02 00:00:00"  # replace with your actual column name

# if date_column_name in df.columns:
#     # Get the date from the first row (or adjust as necessary)
#     excel_date = pd.to_datetime(df[date_column_name].iloc[0])  # Convert to datetime if needed
#     current_date = pd.to_datetime(datetime.now().date())  # Get current date

#     # Step 8: Compare the dates
#     if excel_date.date() == current_date.date():
#         print("The local date matches the date in the Excel sheet.")
#     else:
#         print("The local date does not match the date in the Excel sheet.")
# else:
#     print(f"Column '{date_column_name}' not found in the Excel sheet.")

