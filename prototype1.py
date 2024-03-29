import pandas as pd
import numpy
import itertools
df=pd.read_csv("attg\maths.csv")
df1=pd.read_csv("attg\science.csv")
df2=pd.read_csv("attg\english.csv")
alpha=0.1
Math_array = df.values.flatten().astype(float)
Science_array = df1.values.flatten().astype(float)
English_array = df2.values.flatten().astype(float)
TC = [0.0,0.0,0.0]
TC[0]= (Math_array[0] + Science_array[0] + English_array[0])/3
TC[1]= (Math_array[1] + Science_array[1] + English_array[1])/3
TC[2]= (Math_array[2] + Science_array[2] + English_array[2])/3
interest_index={'Maths':Math_array,'Science':Science_array,'English':English_array}
print(interest_index)
# Function to calculate the total interest index for a daily schedule
def calculate_daily_interest(schedule):
    total_interest = 0
    for i, subject in enumerate(schedule):
        total_interest += interest_index[subject][i]
    return total_interest


# Function to generate all permutations of subjects
def generate_permutations(subjects):
    from itertools import permutations
    return permutations(subjects)


# Function to find the optimal daily timetable
def find_optimal_day():
    subjects = list(interest_index.keys())
    permutations = generate_permutations(subjects)
    max_interest = -float('inf')  # Initialize with negative infinity
    optimal_schedule = None

    for schedule in permutations:
        interest = calculate_daily_interest(schedule)
        if interest > max_interest:
            max_interest = interest
            optimal_schedule = schedule

    return optimal_schedule, max_interest

def repeat_reducer(optimal_schedule):
    for i,subject in enumerate(optimal_schedule):
        interest_index[subject][i]-=alpha
    return interest_index

# Generate the optimal daily timetable and total interest
for i in range(0,6):
    optimal_day, total_interest = find_optimal_day()

    # Print the generated timetable and total interest
    print(*optimal_day, sep=", ")
    x=repeat_reducer(optimal_day)


        
        
