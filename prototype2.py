import pandas as pd
import numpy
import itertools




# Function to calculate the total interest index for a daily schedule
def calculate_daily_interest(schedule):
    total_interest = 0
    for i, subject in enumerate(schedule):
        total_interest += interest_index[subject][i]
    return total_interest

def calculate_daily_interest_2(schedule):
    total_interest = 0
    for i, subject in enumerate(schedule):
        total_interest += interest_index_2[subject][i]
    return total_interest


# Function to generate all permutations of subjects
def generate_permutations(subjects):
    from itertools import permutations
    x= list(permutations(subjects))
    return x

def check_permers(perm1,perm2):
    final_perm = []
    for i in perm1:
        for j in perm2:
            c=0
            for z in range(0,4):
                if i[z]!=j[z]:
                    c+=1
            if c==4:
                final_perm.append((i,j))
    return final_perm
# Function to find the optimal daily timetable
def find_optimal_day():
    subjects = list(interest_index.keys())
    perm1 = generate_permutations(subjects)
    perm2 = generate_permutations(subjects)
    #print(perm1)
    final_perm = check_permers(perm1, perm2)
    max_interest = -float('inf')
    optimal_schedule = None

    for schedule_pair in final_perm:
        interest = calculate_daily_interest(schedule_pair[0])
        interest2 = calculate_daily_interest_2(schedule_pair[1])
        if interest + interest2 > max_interest:
            max_interest = interest + interest2
            optimal_schedule = schedule_pair

    return optimal_schedule, max_interest

def repeat_reducer(optimal_schedule):
    for i,subject in enumerate(optimal_schedule):
        interest_index[subject][i]-=alpha
    return interest_index


def repeat_reducer_2(optimal_schedule):
    for i,subject in enumerate(optimal_schedule):
        interest_index_2[subject][i]-=alpha
    return interest_index_2






df=pd.read_csv("maths.csv")
df1=pd.read_csv("science.csv")
df2=pd.read_csv("english.csv")
df3=pd.read_csv("social.csv")
Math_array = df.values.flatten().astype(float)
Science_array = df1.values.flatten().astype(float)
English_array = df2.values.flatten().astype(float)
Social_array = df3.values.flatten().astype(float)
interest_index={'Maths':Math_array,'Science':Science_array,'English':English_array,'Social':Social_array}
alpha=0.1
df=pd.read_csv("maths_1b.csv")
df1=pd.read_csv("science_1b.csv")
df2=pd.read_csv("english_1b.csv")
df3=pd.read_csv("social_1b.csv")
Math_array = df.values.flatten().astype(float)
Science_array = df1.values.flatten().astype(float)
English_array = df2.values.flatten().astype(float)
Social_array = df3.values.flatten().astype(float)
interest_index_2={'Maths':Math_array,'Science':Science_array,'English':English_array,'Social':Social_array}

# Generate the optimal daily timetable and total interest
class_1A=[]
class_1B=[]
for i in range(0,6):
    optimal_day, total_interest = find_optimal_day()

    # Print the generated timetable and total interest
   # print("Optimal Day:")
    class_1A.append(optimal_day[0])
    class_1B.append(optimal_day[1])
    #print(f"Total Interest: {total_interest}")
    x=repeat_reducer(optimal_day[0])
    y=repeat_reducer_2(optimal_day[1])
print('Class 1A TIME TABLE : ')
df=pd.DataFrame(class_1A)
print(df)
df.to_csv('output.csv', index=False)
print('CLASS 1B TIME TABLE : ')
df=pd.DataFrame(class_1B)
print(df)
df.to_csv('output2.csv', index=False)

        
        
