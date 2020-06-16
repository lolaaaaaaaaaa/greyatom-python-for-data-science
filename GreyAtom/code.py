# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((data, new_record),axis=0)

age=[census[:,0]]
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0,len_1,len_2,len_3,len_4=len(race_0),len(race_1),len(race_2),len(race_3),len(race_4)
race_list=[len_0,len_1,len_2,len_3,len_4]
minority_race=race_list.index(min(race_list))

print(minority_race)

senior_citizens=[]
for array in census:
        if array[0]>60:
                list.append(senior_citizens,array)

senior_citizens=np.array(senior_citizens)

working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)

senior_citizens_len=len(senior_citizens)

avg_working_hours=[working_hours_sum/senior_citizens_len]

print(avg_working_hours)

high=[]
low=[]
for array in census:
    if array[1]>10:
        list.append(high,array)
    elif array[1]<=10:
        list.append(low,array)
high=np.array(high)
low=np.array(low)
avg_pay_high=high[:,7].mean()
avg_pay_low=low[:,7].mean()
print(avg_pay_high,avg_pay_low)


