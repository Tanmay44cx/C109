import pandas as pd
import statistics as st

df=pd.read_csv("StudentsPerformance.csv")
math_list=df["math score"].tolist()

math_mean=st.mean(math_list)
math_median=st.median(math_list)
math_mode=st.mode(math_list)

print(math_mean,math_median,math_mode)

math_stdev=st.stdev(math_list)

print(math_stdev)

math_stdev1_start=math_mean-math_stdev
math_stdev1_end=math_mean+math_stdev

math_stdev2_start=math_mean-(2*math_stdev)
math_stdev2_end=math_mean+(2*math_stdev)

math_stdev3_start=math_mean-(3*math_stdev)
math_stdev3_end=math_mean+(3*math_stdev)

math_list_within_stdev1=[result for result in math_list if result>math_stdev1_start and result<math_stdev1_end]
math_list_within_stdev2=[result for result in math_list if result>math_stdev2_start and result<math_stdev2_end]
math_list_within_stdev3=[result for result in math_list if result>math_stdev3_start and result<math_stdev3_end]

percent_data_within_stdev1=(len(math_list_within_stdev1)/len(math_list))*100
percent_data_within_stdev2=(len(math_list_within_stdev2)/len(math_list))*100
percent_data_within_stdev3=(len(math_list_within_stdev3)/len(math_list))*100

print(percent_data_within_stdev1)
print(percent_data_within_stdev2)
print(percent_data_within_stdev3)



