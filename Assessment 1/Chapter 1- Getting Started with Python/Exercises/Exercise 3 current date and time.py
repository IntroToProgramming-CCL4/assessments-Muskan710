# Import the datetime module for datetime opertation.
import datetime 
#Get the current date and time .
current_date_time=datetime.datetime.now()
#format the current date and time as a string in the format"YYYY-MM-DD HH:MM:SS
formatted_date_time=current_date_time.strftime("%Y-%m-%d %H:%M:%S")
# print the formatted date and time.
print("current date and time:",formatted_date_time)