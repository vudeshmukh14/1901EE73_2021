import csv
from numpy import False_
import pandas as pd

def feedback_not_submitted():

	
	ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3:'practical'}
	output_file_name = "course_feedback_remaining.xlsx" 

	# reading csv files of course_master, feedback_submitted and studentinfo into a csv reader object
	# and coverting it into dictionary for easy and fast access 
	dict_course_master={}
	with open(r"course_master_dont_open_in_excel.csv", 'r') as course_master:
		course_master_reader=csv.reader(course_master)
		dict_course_master={rows[0]:rows[2] for rows in course_master_reader}

	dict_info={}
	with open(r"studentinfo.csv", 'r') as info_file:
		info_reader=csv.reader(info_file)
		dict_info={rows[1]:[rows[0], rows[8], rows[9], rows[10]] for rows in info_reader}

	dict_feedback={}
	with open(r"course_feedback_submitted_by_students.csv", 'r') as feedback_file:
		feedback_reader=csv.reader(feedback_file)
		for rows in feedback_reader:
			if rows[3] in dict_feedback:
				dict_feedback[rows[3]].append([rows[4], rows[5]])
			else :
				dict_feedback[rows[3]]=[[rows[4], rows[5]]]

	# initializing an empty pandas dataframe to which all the rows for remaining feedback will be appended
	column_names=["rollno", "register_sem", "schedule_sem", "subno", "Name", "email", "aemail", "contact"]
	df=pd.DataFrame(columns=column_names)
	# print(df)

	# iterating on all rows of course_registered csv file
	with open(r"course_registered_by_all_students.csv", 'r') as registered_file:

		registered_reader=csv.reader(registered_file)

		for row in registered_reader:

			if row[0]=="rollno":
				continue
			
			# taking LTP of each course and splitting it on "-"
			ltp=dict_course_master[row[3]].split("-")

			# if course has lectures
			if ltp[0]!="0":
				if row[0] in dict_feedback.keys():
					flag=False
					for feedback in dict_feedback[row[0]]:
						# if the feedback for particular roll number, subject number and feedback type exists
						if feedback[0]==row[3] and feedback[1]=="1":
							flag=True
							break
					# if feedback doesn't exists
					if flag==False:
						if row[0] in dict_info.keys():
							df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":dict_info[row[0]][0], "email":dict_info[row[0]][1], "aemail":dict_info[row[0]][2], "contact":dict_info[row[0]][3]}, ignore_index=True)
						else :
							df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":"NA_IN_STUDENTINFO", "email":"NA_IN_STUDENTINFO", "aemail":"NA_IN_STUDENTINFO", "contact":"NA_IN_STUDENTINFO"}, ignore_index=True)
				else :
					if row[0] in dict_info.keys():
						df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":dict_info[row[0]][0], "email":dict_info[row[0]][1], "aemail":dict_info[row[0]][2], "contact":dict_info[row[0]][3]}, ignore_index=True)
					else :
						df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":"NA_IN_STUDENTINFO", "email":"NA_IN_STUDENTINFO", "aemail":"NA_IN_STUDENTINFO", "contact":"NA_IN_STUDENTINFO"}, ignore_index=True)
					
			# if course has tutorials
			if ltp[1]!="0":
				if row[0] in dict_feedback.keys():
					flag=False
					for feedback in dict_feedback[row[0]]:
						if feedback[0]==row[3] and feedback[1]=="2":
							flag=True
							break
					if flag==False:
						if row[0] in dict_info.keys():
							df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":dict_info[row[0]][0], "email":dict_info[row[0]][1], "aemail":dict_info[row[0]][2], "contact":dict_info[row[0]][3]}, ignore_index=True)
						else :
							df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":"NA_IN_STUDENTINFO", "email":"NA_IN_STUDENTINFO", "aemail":"NA_IN_STUDENTINFO", "contact":"NA_IN_STUDENTINFO"}, ignore_index=True)
				else :
					if row[0] in dict_info.keys():
						df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":dict_info[row[0]][0], "email":dict_info[row[0]][1], "aemail":dict_info[row[0]][2], "contact":dict_info[row[0]][3]}, ignore_index=True)
					else :
						df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":"NA_IN_STUDENTINFO", "email":"NA_IN_STUDENTINFO", "aemail":"NA_IN_STUDENTINFO", "contact":"NA_IN_STUDENTINFO"}, ignore_index=True)

			# if course has practicals
			if ltp[2]!="0":
				if row[0] in dict_feedback.keys():
					flag=False
					for feedback in dict_feedback[row[0]]:
						if feedback[0]==row[3] and feedback[1]=="3":
							flag=True
							break
					if flag==False:
						if row[0] in dict_info.keys():
							df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":dict_info[row[0]][0], "email":dict_info[row[0]][1], "aemail":dict_info[row[0]][2], "contact":dict_info[row[0]][3]}, ignore_index=True)
						else :
							df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":"NA_IN_STUDENTINFO", "email":"NA_IN_STUDENTINFO", "aemail":"NA_IN_STUDENTINFO", "contact":"NA_IN_STUDENTINFO"}, ignore_index=True)
				else :
					if row[0] in dict_info.keys():
						df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":dict_info[row[0]][0], "email":dict_info[row[0]][1], "aemail":dict_info[row[0]][2], "contact":dict_info[row[0]][3]}, ignore_index=True)
					else :
						df=df.append({"rollno":row[0], "register_sem":row[1], "schedule_sem":row[2], "subno":row[3], "Name":"NA_IN_STUDENTINFO", "email":"NA_IN_STUDENTINFO", "aemail":"NA_IN_STUDENTINFO", "contact":"NA_IN_STUDENTINFO"}, ignore_index=True)

	# print(df)

	# converting the dataframe into excel file
	df.to_excel(output_file_name, index=False)




feedback_not_submitted()

# I have considered the logic, for ex: if a course has LTP as 3-2-2
# and feedback exists for only one feedback type then there are two
# entries for the same roll number
# Therefore there will be some duplicate entries and number of rows will be more