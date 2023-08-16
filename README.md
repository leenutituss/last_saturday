# last_saturday
Last Saturday of Month Finder
This code snippet is designed to find the last Saturday of a specified month and year, along with calculating the total number of Saturdays in that month.

## Usage
Call the last_saturday_and_total function, passing a string representing the input date in the format 'MMYYYY'.
The function will return the last Saturday date and the total number of Saturdays in the specified month.
Example usage:
from calendar import monthcalendar

def last_saturday_and_total(input_date):
    # ... (rest of the function code)

input_date = '062023'
last_saturday, total_saturdays = last_saturday_and_total(input_date)
print(f"Last Saturday: {last_saturday}")
print(f"Total Saturdays: {total_saturdays}")
## Function Explanation
The last_saturday_and_total function takes an input date in the 'MMYYYY' format and performs the following steps:

Extracts the month and year from the input date.
Uses the monthcalendar function from the calendar module to generate a matrix representing the calendar month.
Determines the last Saturday date based on the generated matrix.
Calculates the total number of Saturdays in the month.
Parameters
input_date (str): A string representing the input date in the 'MMYYYY' format.
Return Values
last_saturday (int): The date of the last Saturday in the specified month.
total_saturdays (int): The total number of Saturdays in the specified month.
Example
For the input date '062023', the function will return:
Last Saturday: 24062023
Total Saturdays: 4






