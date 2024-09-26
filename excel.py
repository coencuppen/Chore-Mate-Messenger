import os
import requests
import pandas as pd
from datetime import datetime

# Step 1: Correct Google Sheets download URL format
url = "https://docs.google.com/spreadsheets/d/1KvUvxK7MPfCXKifQ_biml9cmto6CcQ8UPR5lm4kVwjc/export?format=xlsx"

# Step 2: Define the local file path
huistaakRoosterPath = "huistaakRooster.xlsx"

# Step 3: Check if the file already exists
if not os.path.exists(huistaakRoosterPath):
    # Step 4: Download the Excel file
    response = requests.get(url)
    
    # Step 5: Save the file locally
    with open(huistaakRoosterPath, "wb") as file:
        file.write(response.content)
    
    print(f'Downloaded: {huistaakRoosterPath}')
else:
    print(f'File already exists: {huistaakRoosterPath}')

# Step 6: Read the Excel file into a Pandas DataFrame
df = pd.read_excel(huistaakRoosterPath, engine='openpyxl')

date_column_name = f"2024-09-02 00:00:00"  # replace with your actual column name

if date_column_name in df.columns:
    # Get the date from the first row (or adjust as necessary)
    excel_date = pd.to_datetime(df[date_column_name].iloc[0])  # Convert to datetime if needed
    current_date = pd.to_datetime(datetime.now().date())  # Get current date

    # Step 8: Compare the dates
    if excel_date.date() == current_date.date():
        print("The local date matches the date in the Excel sheet.")
    else:
        print("The local date does not match the date in the Excel sheet.")
else:
    print(f"Column '{date_column_name}' not found in the Excel sheet.")

print(df)