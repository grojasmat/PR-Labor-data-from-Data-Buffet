
#Gustavo Rojas-Matute #
#data buffet example - Extracting Puerto Rico Labor Data from Data Buffet ##

import sys
import os
import dbapi
import pandas
import numpy as np
from datetime import datetime
def prompt(prompt_text:str):
     ret = None
     while ret is None:
         ret = input(f'{prompt_text} : ').strip()
     return ret
print('\nGet your API heys here: https://economy.com/myeconomy/api-key-info\n')
access_key = prompt('Please enter your access key')
encryption_key = prompt('Please enter your encryption key')

# instantiate the api class
api = dbapi.DataBuffetAPI(access_key,encryption_key)
# locate available series to test with
#search = api.search(query='SA',rows=2)

def get_series(series_id, access_key, encryption_key):
    # Instantiate the API class
    api = dbapi.DataBuffetAPI(access_key, encryption_key)
    # Retrieve the series data
    series_data = api.get_series(series_id)
    return series_data


# Extend the list of series
lh = get_series("ELH.PR", access_key, encryption_key)
construction = get_series("E23.PR", access_key, encryption_key)
prof_bus = get_series("EPS.PR", access_key, encryption_key)
retail = get_series("ERT.PR", access_key, encryption_key)
edu_health = get_series("EEH.PR", access_key, encryption_key)
wholesale = get_series("E42.PR", access_key, encryption_key)
government = get_series("EGVSL.PR", access_key, encryption_key)
finance = get_series("EFI.PR", access_key, encryption_key)
trans_ware = get_series("ETU.PR", access_key, encryption_key)
manufacturing = get_series("EMF.PR", access_key, encryption_key)
# Extend the DataFrame to include all series
data = {
    "Labor_Hours": lh,
    "Construction": construction,
    "Professional_Business": prof_bus,
    "Retail": retail,
    "Education_Health": edu_health,
    "Wholesale": wholesale,
    "Government": government,
    "Finance": finance,
    "Transportation_Warehousing": trans_ware,
    "Manufacturing": manufacturing
}
print(lh)
print(construction)
print(manufacturing)
# Print all variables included in the DataFrame
print("Variables included in the DataFrame:")
for variable in data.keys():
    print(variable)

df = pandas.DataFrame(data)

print(df)

# Generate a date range from 1990-01-31 to 2025-03-31 with monthly frequency
date_range = pandas.date_range(start="1990-01-31", end="2025-03-31", freq="M")

# Add the date range as the first column in the DataFrame
df.insert(0, "Date", date_range)

print(df)

# Convert the DataFrame to a CSV file and save it in the specified directory
output_path = r"C:\Users\xxx\PR_labor_test.csv" #edit the path
df.to_csv(output_path, index=False)
print(f"DataFrame has been saved to {output_path}")



