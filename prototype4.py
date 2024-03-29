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

def calculate_daily_interest_3(schedule):
    total_interest = 0
    for i, subject in enumerate(schedule):
        total_interest += interest_index_3[subject][i]
    return total_interest
# Function to generate all permutations of subjects

def generate_permutations(subjects):
    from itertools import permutations
    x= list(permutations(subjects))
    return x

def check_permers(perm1,perm2,perm3):
    final_perm = []
    for i in perm1:
        for j in perm2:
            for k in perm3:
                c=0
                for z in range(0,6):
                    if i[z]!=j[z] and i[z]!=k[z] and j[z]!=k[z]:
                        c+=1
            if c==6:
                final_perm.append((i,j,k))
    return final_perm



# Function to find the optimal daily timetable
def find_optimal_day():
    subjects = list(interest_index.keys())
    perm1 = generate_permutations(subjects)
    perm2 = perm1
    perm3=perm1
    final_perm = check_permers(perm1,perm2,perm3)
    max_interest = -float('inf')
    optimal_schedule = None

    for schedule_pair in final_perm:
        interest = calculate_daily_interest(schedule_pair[0])
        interest2 = calculate_daily_interest_2(schedule_pair[1])
        interest3 = calculate_daily_interest_3(schedule_pair[2])
        if interest + interest2 + interest3 > max_interest:
            max_interest = interest + interest2 + interest3
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

def repeat_reducer_3(optimal_schedule):
    for i,subject in enumerate(optimal_schedule):
        interest_index_3[subject][i]-=alpha
    return interest_index_3





df=pd.read_csv("maths.csv")
df1=pd.read_csv("science.csv")
df2=pd.read_csv("english.csv")
df3=pd.read_csv("social.csv")
df4=pd.read_csv('secondlang.csv')
df5=pd.read_csv('thirdlang.csv')
Math_array = df.values.flatten().astype(float)
Science_array = df1.values.flatten().astype(float)
English_array = df2.values.flatten().astype(float)
Social_array = df3.values.flatten().astype(float)
SecondLang_array = df4.values.flatten().astype(float)
ThirdLang_array = df5.values.flatten().astype(float)
interest_index={'Maths':Math_array,'Science':Science_array,'English':English_array,'Social':Social_array,'SecondLang':SecondLang_array,'ThirdLang':ThirdLang_array}
alpha=0.1
df=pd.read_csv("maths_1b.csv")
df1=pd.read_csv("science_1b.csv")
df2=pd.read_csv("english_1b.csv")
df3=pd.read_csv("social_1b.csv")
df4=pd.read_csv('secondlang_1b.csv')
df5=pd.read_csv('thirdlang_1b.csv')
Math_array = df.values.flatten().astype(float)
Science_array = df1.values.flatten().astype(float)
English_array = df2.values.flatten().astype(float)
Social_array = df3.values.flatten().astype(float)
SecondLang_array = df4.values.flatten().astype(float)
ThirdLang_array = df5.values.flatten().astype(float)
interest_index_2={'Maths':Math_array,'Science':Science_array,'English':English_array,'Social':Social_array,'SecondLang':SecondLang_array,'ThirdLang':ThirdLang_array}


df=pd.read_csv("maths_1c.csv")
df1=pd.read_csv("science_1c.csv")
df2=pd.read_csv("english_1c.csv")
df3=pd.read_csv("social_1c.csv")
df4=pd.read_csv('secondlang_1c.csv')
df5=pd.read_csv('thirdlang_1c.csv')
Math_array = df.values.flatten().astype(float)
Science_array = df1.values.flatten().astype(float)
English_array = df2.values.flatten().astype(float)
Social_array = df3.values.flatten().astype(float)
SecondLang_array = df4.values.flatten().astype(float)
ThirdLang_array = df5.values.flatten().astype(float)
interest_index_3={'Maths':Math_array,'Science':Science_array,'English':English_array,'Social':Social_array,'SecondLang':SecondLang_array,'ThirdLang':ThirdLang_array}
# Generate the optimal daily timetable and total interest
class_1A=[]
class_1B=[]
class_1C=[]
for i in range(0,6):
    optimal_day, total_interest = find_optimal_day()
    print(optimal_day,total_interest)
    # Print the generated timetable and total interest
   # print("Optimal Day:")
    class_1A.append(optimal_day[0])
    class_1B.append(optimal_day[1])
    class_1C.append(optimal_day[2])
    #print(f"Total Interest: {total_interest}")
    x=repeat_reducer(optimal_day[0])
    y=repeat_reducer_2(optimal_day[1])
    z=repeat_reducer_3(optimal_day[2])
print('Class 1A TIME TABLE : ')
df=pd.DataFrame(class_1A)
print(df)
df.to_csv('output.csv', index=False)
print('CLASS 1B TIME TABLE : ')
df=pd.DataFrame(class_1B)
print(df)
df.to_csv('output2.csv', index=False)
df=pd.DataFrame(class_1C)
print(df)
df.to_csv('output2.csv', index=False)

        
        
