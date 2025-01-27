# Instructions:
# 1. **Remove the TODO comment and pass statement** once you’ve completed the function implementation.
#    - The TODO and pass are placeholders indicating that the function is not yet complete.
#    - Once the function is implemented, these should be removed to keep the code clean.
# 
# 2. **Best Coding Practices**:
#    - In professional programming, finalizing the code means removing unnecessary placeholders.
#    - This ensures your code is ready for review, testing, and does not contain clutter.
# 
# 3. **Adding Docstrings**:
#    - After removing TODO and pass, add a **docstring** for each function.
#    - The docstring should explain the function’s purpose, parameters, and expected output.
#    - Proper documentation improves code readability and helps with debugging and maintenance.

def read_weather_data(file_path: str):
    file = open(file_path, 'r')
    weather_data = file.read()
    lines = weather_data.splitlines()
    data = []
    for row in lines:
        split_row = row.split(',')
        my_tuple = tuple(split_row)
        data.append(my_tuple) 
     
    return data
    '''Takes a text file with a data on each line, and converts each line into a tuple that is stored in a list, then that list is returned'''

    
def calculate_average_temperature(data):
    average = []
    for row in data:
        average.append(int(row[1]))
    total = 0
    for num in average:
        total += num
    temp = total / len(average)
    
    return temp  
    '''Takes data from a text file and uses the second index in each tuple to calculate the average temperature'''
    

def calculate_total_rainfall(data):
    rainfall = []
    for row in data:
        rainfall.append(float(row[2]))
    total = 0
    for num in rainfall:
        total += num
    
    return total
    """takes data from a text file, using the third index from each tuple it takes the amount of rainfall from each day and adds together to return the total rainfall
    """
    

def find_highest_temperature(data):
    temp = []
    for row in data:
        temp.append(int(row[1]))
    high = max(temp)
    for row in data:
        if row[1] == str(high):
            high_temp = row[0]
    
    return (high_temp, high)
    """Takes data froma text file, isolates each temp from each day into a list and finds the max temp,
    then checks the whole data for the date with the highest temp, returns day temp"""



def find_lowest_temperature(data):
    temp = []
    for row in data:
        temp.append(int(row[1]))
    low = min(temp)
    for row in data:
        if row[1] == str(low):
            low_temp = row[0]
    
    return (low_temp, low)
    """Takes data from a text file, isolates temp into list and finds min temp,
    then checks whole data for the date with the lowest temp, returns day, temp"""
    

def find_day_with_most_rainfall(data):
    rainfall = []
    for row in data:
        rainfall.append(float(row[2]))
    high = max(rainfall)
    for row in data:
        if row[2] == str(high):
            high_rain = row[0]
    
    return (high_rain, high)
    """takes data froma text file, isolates rainfall into a list and finds max rainfall,
    then check whole data for the date with the most rainfall, returns day, rainfall
    """





