import os
import requests
import pandas as pd
from datetime import datetime

# Step 1: Correct Google Sheets download URL format
huistakenURL = "https://docs.google.com/spreadsheets/d/1KvUvxK7MPfCXKifQ_biml9cmto6CcQ8UPR5lm4kVwjc/export?format=xlsx"
afwasRoosterURL = "https://docs.google.com/spreadsheets/d/1YO39jobgWjv6uNDabw3qdShkKv3RSR1W04Ux3q1h3yg/edit?gid=873229454#gid=873229454"

# Step 2: Define the local file path
huistaakRoosterPath = "huistaakRooster.xlsx"
afwasRoosterPath = "afwasrooster.xlsx"

# Step 3: Check if the file already exists
def getExcelFiles(url, path):
    if not os.path.exists(path):
        # Step 4: Download the Excel file
        print(f"downlaoding url:{url}")
        response = requests.get(url)
        
        # Step 5: Save the file locally
        with open(path, "wb") as file:
            file.write(response.content)
        
        print(f'Downloaded: {path}')
    else:
        print(f'File already exists: {path}')

def getTodaysDishWasher():
    df = pd.read_excel(afwasRoosterPath, engine='openpyxl')
    print(df)



def init():
    getExcelFiles(huistakenURL, huistaakRoosterPath)
    getExcelFiles(afwasRoosterURL, afwasRoosterPath)



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

