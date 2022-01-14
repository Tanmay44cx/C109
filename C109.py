import pandas as pd
import statistics as st

df=pd.read_csv("data.csv")
height_list=df["Height(Inches)"].tolist()

height_mean=st.mean(height_list)
height_median=st.median(height_list)
height_mode=st.mode(height_list)

print(height_mean,height_median,height_mode)

height_stdev=st.stdev(height_list)

print(height_stdev)

height_stdev1_start=height_mean-height_stdev
height_stdev1_end=height_mean+height_stdev

height_stdev2_start=height_mean-(2*height_stdev)
height_stdev2_end=height_mean+(2*height_stdev)

height_stdev3_start=height_mean-(3*height_stdev)
height_stdev3_end=height_mean+(3*height_stdev)

height_list_within_stdev1=[result for result in height_list if result>height_stdev1_start and result<height_stdev1_end]
height_list_within_stdev2=[result for result in height_list if result>height_stdev2_start and result<height_stdev2_end]
height_list_within_stdev3=[result for result in height_list if result>height_stdev3_start and result<height_stdev3_end]

percent_data_within_stdev1=(len(height_list_within_stdev1)/len(height_list))*100
percent_data_within_stdev2=(len(height_list_within_stdev2)/len(height_list))*100
percent_data_within_stdev3=(len(height_list_within_stdev3)/len(height_list))*100

print(percent_data_within_stdev1)
print(percent_data_within_stdev2)
print(percent_data_within_stdev3)



