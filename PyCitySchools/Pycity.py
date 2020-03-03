# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


length=len(school_data_complete['school_name'].unique())
total_students=len(school_data_complete)
budget=school_data['budget'].sum()
average_math=school_data_complete['math_score'].mean()
average_reading=school_data_complete['reading_score'].mean()
math_greater=student_data[student_data["math_score"]>=70]
num_math=len(math_greater)
passing_math=num_math/total_students*100
reading_greater=student_data[student_data["reading_score"]>=70]
num_reading=len(reading_greater)
passing_reading=num_reading/total_students*100
overall_passing=(average_math+average_reading)/2


district_summary = pd.DataFrame({"Total Schools": [length],
                              "Total Students": total_students,
                              "Total Budget": '${:,.2f}'.format(budget),
                              "Average Math Score": average_math,
                             "Average Reading Score":average_reading,
                              "% Passing Math":passing_math,
                              "% Passing Reading":passing_reading,
                              "% Overall Passing Rate":overall_passing})
#First result
district_summary             

name=school_data_complete.groupby("school_name")
totalsize=name.size()
totalbudget=name["budget"].first()
totaltype=name['type'].first()
perstudent=totalbudget/totalsize
av_math=name['math_score'].mean()
av_reading=name['reading_score'].mean()
math_greater2=student_data[student_data["math_score"]>=70].groupby("school_name").size()
passmath=math_greater2/totalsize*100
reading_greater2=student_data[student_data["reading_score"]>=70].groupby("school_name").size()
passreading=reading_greater2/totalsize*100
overall=(passmath+passreading)/2

school_summary=pd.DataFrame({"School Type": totaltype,
                              "Total Students": totalsize,
                              "Total Budget":totalbudget,
                              "Per Student Budget":perstudent,
                              "Average Math Score": av_math,
                             "Average Reading Score":av_reading,
                              "% Passing Math":passmath,
                              "% Passing Reading":passreading,
                              "% Overall Passing Rate":overall})
school_summary['Total Budget']=school_summary['Total Budget'].map("${:,}".format)
school_summary['Per Student Budget']=school_summary['Per Student Budget'].map("${:.2f}".format)

#second result
school_summary.sort_values(by='% Overall Passing Rate',ascending=False).head()
#third result
school_summary.sort_values(by='% Overall Passing Rate',ascending=True).head()


#Math Scores by Grade

grade9=school_data_complete[school_data_complete["grade"]=='9th'].groupby("school_name")
grade10=school_data_complete[school_data_complete["grade"]=='10th'].groupby("school_name")
grade11=school_data_complete[school_data_complete["grade"]=='11th'].groupby("school_name")
grade12=school_data_complete[school_data_complete["grade"]=='12th'].groupby("school_name")
av_math9=grade9["math_score"].mean()
av_math10=grade10["math_score"].mean()
av_math11=grade11["math_score"].mean()
av_math12=grade12["math_score"].mean()
math_summary=pd.DataFrame({"9th": av_math9,
                              "10th": av_math10,
                              "11th":av_math11,
                              "12th":av_math12,})
math_summary

#Reading Score by Grade

av_reading9=grade9["reading_score"].mean()
av_reading10=grade10["reading_score"].mean()
av_reading11=grade11["reading_score"].mean()
av_reading12=grade12["reading_score"].mean()
reading_summary=pd.DataFrame({"9th":av_reading9,
                              "10th":av_reading10,
                              "11th":av_reading11,
                              "12th":av_reading12,})
reading_summary

#Scores by School Spending
# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]

#----------------to change the objects back to int
school_summary=pd.DataFrame({"School Type": totaltype,
 "Total Students": totalsize,
 "Total Budget":totalbudget,
 "Per Student Budget":perstudent,
 "Average Math Score": av_math,
"Average Reading Score":av_reading,
 "% Passing Math":passmath,
 "% Passing Reading":passreading,
 "% Overall Passing Rate":overall})
#--------------------------------
#Scores by School Spending
school_summary['Spending Ranges (Per Student)']=pd.cut(school_summary['Per Student Budget'],spending_bins,labels=group_names)

new_school=school_summary.groupby('Spending Ranges (Per Student)')
newmath=new_school['Average Math Score'].mean()
newreading=new_school['Average Reading Score'].mean()
newpassing_math=new_school['% Passing Math'].mean()
newpassing_reading=new_school['% Passing Reading'].mean()
newoverall_passing=new_school['% Overall Passing Rate'].mean()
scores_spending=pd.DataFrame({"Average Math Score": newmath,
                             "Average Reading Score":newreading,
                              "% Passing Math":newpassing_math,
                              "% Passing Reading":newpassing_reading,
                              "% Overall Passing Rate":newoverall_passing
                             })

scores_spending

#Scores by School Size

# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
school_summary['School Size']=pd.cut(school_summary['Total Students'],size_bins,labels=group_names)
new_schoolsize=school_summary.groupby('School Size')
newmath1=new_schoolsize['Average Math Score'].mean()
newreading1=new_schoolsize['Average Reading Score'].mean()
newpassing_math1=new_schoolsize['% Passing Math'].mean()
newpassing_reading1=new_schoolsize['% Passing Reading'].mean()
newoverall_passing1=new_schoolsize['% Overall Passing Rate'].mean()

scores_size=pd.DataFrame({"Average Math Score": newmath1,
                             "Average Reading Score":newreading1,
                              "% Passing Math":newpassing_math1,
                              "% Passing Reading":newpassing_reading1,
                              "% Overall Passing Rate":newoverall_passing1
                             })
scores_size

#Scores by School Type
school_type=school_summary.groupby('School Type')
newmath2=school_type['Average Math Score'].mean()
newreading2=school_type['Average Reading Score'].mean()
newpassing_math2=school_type['% Passing Math'].mean()
newpassing_reading2=school_type['% Passing Reading'].mean()
newoverall_passing2=school_type['% Overall Passing Rate'].mean()
school_type_summary=pd.DataFrame({"Average Math Score": newmath2,
                             "Average Reading Score":newreading2,
                              "% Passing Math":newpassing_math2,
                              "% Passing Reading":newpassing_reading2,
                              "% Overall Passing Rate":newoverall_passing2
                             })
school_type_summary
